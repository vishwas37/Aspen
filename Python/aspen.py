import hashlib


class AspenBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + \
            "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Vishwas sends 37 AC to Vivek"
t2 = "Vivek sends 18 AC to Vishnu"
t3 = "Smitha sends 7 AC to Suresh"
t4 = "Mohammad sends 3 AC to Gagan"
t5 = "David sends 16 AC to Payal"
t6 = "Michael sends 20 AC to Amit"

initial_block = AspenBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = AspenBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = AspenBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)
