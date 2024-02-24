import subprocess

def generate_proof(value, proof_file):
    subprocess.run(["python", "3_membership_non_membership_proof_gen.py", "--merkle_leaves_file", "merkle_leaves.json",
                    "--value", str(value), "--proof_file", proof_file])

def verify_proof(proof_file):
    subprocess.run(["python", "4_membership_non_membership_proof_verifier.py", "--merkle_root_file", "merkle_root.json",
                    "--proof_file", proof_file])

if __name__ == "__main__":
    my_id = 19015550
    values_proof_files = [(9, "membership_proof.json"),
                          (10, "non_membership_proof.json"),
                          (-1, "min_proof.json"),
                          (9999999999999999999999999999999, "max_proof.json"),
                          (my_id % 99, "my_id_proof.json")]
    for value, proof_file in values_proof_files:
        generate_proof(value, proof_file)
        verify_proof(proof_file)
