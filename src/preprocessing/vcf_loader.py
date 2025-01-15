import os
import hail as hl
from ..utils.logging_utils import log_step

def verify_vcf_file(vcf_path):
    """Verify VCF file exists and return basic information"""
    file_info = {
        "exists": os.path.exists(vcf_path),
        "size_mb": None
    }
    
    if file_info["exists"]:
        file_info["size_mb"] = os.path.getsize(vcf_path) / (1024 * 1024)
    
    return file_info

def load_vcf(vcf_path, reference_genome='GRCh38', min_partitions=8):
    """Load VCF file with error handling and retries"""
    file_info = verify_vcf_file(vcf_path)
    if not file_info["exists"]:
        raise FileNotFoundError(f"VCF file not found: {vcf_path}")
        
    log_step(f"Loading VCF file: {vcf_path}")
    try:
        mt = hl.import_vcf(
            vcf_path,
            force_bgz=True,
            reference_genome=reference_genome,
            skip_invalid_loci=True,
            min_partitions=min_partitions
        )
        return mt
        
    except Exception as e:
        log_step(f"First attempt failed: {e}")
        log_step("Trying alternative loading options...")
        
        # Second attempt with different options
        mt = hl.import_vcf(
            vcf_path,
            force_bgz=True,
            reference_genome=reference_genome,
            skip_invalid_loci=True,
            header_file=vcf_path
        )
        return mt