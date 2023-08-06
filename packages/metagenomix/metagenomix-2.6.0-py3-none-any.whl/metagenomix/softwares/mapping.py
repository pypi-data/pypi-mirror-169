# ----------------------------------------------------------------------------
# Copyright (c) 2022, Franck Lejzerowicz.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from metagenomix._io_utils import caller, io_update


def bwa():
    cmd = 'bwa index -p %s/index %s\n' % (out_dir, contigs)
    cmd += 'bwa mem -p %s/index %s' % (out_dir, fastqs)
    cmd += ' | samtools view -bh'
    cmd += ' | samtools sort -o %s/%s\n' % (out_dir, bam)
    cmd += 'samtools index %s %s\n' % (bam, bai)


def bowtie2():
    cmd = 'bwa index -p %s/index %s\n' % (out_dir, contigs)
    cmd += 'bwa mem -p %s/index %s' % (out_dir, fastqs)
    cmd += ' | samtools view -bh'
    cmd += ' | samtools sort -o %s/%s\n' % (out_dir, bam)
    cmd += 'samtools index %s %s\n' % (bam, bai)


def spades(self):
    pass


def metawrap_refine(self):
    pass


def mapping(self):
    """Mapping would be a rather specific process that generically consists
    in aligning reads that can be raw, filtered, or for a specific scope (
    e.g., that were used to re-assemble a MAGs or specific proteins).

    It can be done using different aligners, such as BWA, bowtie2, minimap2,
    bbmap, or others, but all should yield a .sam file that can be piped in
    to samtools in order to obtain one .bam file and one .bai file per
    mapping. These files are then possibly used by several other softwares.

    Parameters
    ----------
    self : Commands class instance
        Contains all the attributes needed for binning on the current sample
    """
    # This function splits the name of the software and calls as function
    # the last underscore-separated field (which is in this module)
    module_call = caller(self, __name__)
    module_call(self)


def previous_mapper(self):
    refs = {}
    fastqs, group_fps = self.config.fastq, self.inputs[self.pool]
    if self.soft.prev == 'drep':
        for algo, fp in self.inputs[self.pool].items():
            ref_fasta = '%s.fa' % fp
            if not isfile(ref_fasta):
                cmd = 'if [ ! -f %s ]; then cat %s/*.fa > %s; fi' % (
                    ref_fasta, fp, ref_fasta)
                self.outputs['cmds'].setdefault(
                    (self.pool, algo), []).append(cmd)
            refs[algo] = ref_fasta
    elif self.soft.prev == 'metawrap_reassemble':
        # needs revision...
        refs = {'': glob.glob(self.inputs[self.pool][self.sam][1])}
    elif self.soft.prev == 'spades':
        refs = {group: fps[1] for group, fps in group_fps.items()}

    self.outputs['outs'] = {}
    for group, fasta in refs.items():
        self.outputs['outs'][group] = {}
        out_dir = '%s/%s' % (self.dir, self.pool)
        if group:
            out_dir += '/%s' % group
        self.outputs['dirs'].append(out_dir)
        for sam in self.pools[self.pool][group]:
            bam_out = '%s/%s.bam' % (out_dir, sam)
            self.outputs['outs'][group][sam] = bam_out
            cmd = 'minimap2'
            cmd += ' -a -x sr'
            cmd += ' %s' % fasta
            cmd += ' %s' % fastqs[sam][0]
            cmd += ' %s' % fastqs[sam][1]
            cmd += ' | samtools view -F 0x104 -b -'
            cmd += ' | samtools sort -o %s - ' % bam_out
            if not isfile(bam_out) or self.config.force:
                self.outputs['cmds'].setdefault(
                    (self.pool, group), []).append(cmd)
            bam_out_bai = '%s.bai' % bam_out
            cmd = 'samtools index %s' % bam_out
            if not isfile(bam_out_bai) or self.config.force:
                self.outputs['cmds'].setdefault(
                    (self.pool, group), []).append(cmd)
            io_update(self, i_f=([fasta] + fastqs[sam]),
                      o_f=[bam_out, bam_out_bai])


def prep_map__spades_prodigal(self):
    if 'prodigal' not in self.softs or 'mapping' not in self.softs:
        return None
    if self.softs['prodigal'].prev != 'spades':
        return None
    if self.softs['mapping'].prev != 'spades':
        return None
    prodigals_fps = self.softs['prodigal'].outputs
    sams_fps = self.softs['mapping'].outputs
    group_fps = self.inputs[self.pool]
    self.outputs['outs'] = {}
    for group, fps in group_fps.items():
        self.outputs['outs'][group] = {}
        for sam in self.pools[self.pool][group]:
            bam = sams_fps[self.pool][group][sam]
            prot = prodigals_fps[self.pool][group][1]
            out_dir = '%s/%s/%s' % (self.dir, self.pool, sam)
            out = '%s/reads.txt' % out_dir
            if not isfile(out):
                cmd = 'pysam_reads_to_prodigal.py \\\n'
                cmd += '-prodigal %s \\\n' % prot
                cmd += '-bam %s \\\n' % bam
                cmd += '-out %s\n' % out
                self.outputs['cmds'].setdefault(
                    (self.pool, group), []).append(cmd)
            self.outputs['outs'][group][sam] = out
            io_update(self, i_f=[prot, bam, out])


def map__cazy_spades(self):
    pass


def map__cazy_macsyfinder(self):
    pass


def map__spades_bins(self):
    pass


def map__drep(self):
    pass

