import pathlib
import re
import bitarray  # Efficient bit storage

def write_output(string: str) -> None:
    """
    Appends a given string to the output file `outputPS03.txt`.

    Args:
        string (str): The string to write to the file.

    Runtime Analysis:
        - File I/O operations dominate the runtime.
        - Opening, writing, and closing the file is O(1), assuming the file system handles the operations efficiently.
    """
    # Construct the output file path
    output_file_path = pathlib.Path(__file__).parent / "outputPS03.txt"

    # Ensure the string ends with a newline character
    if not string.endswith("\n"):
        string += '\n'

    # Append the string to the file
    with open(output_file_path, "a") as output:
        output.write(string)


class BloomFilter:
    def __init__(self, size: int = 1000) -> None:
        """
        Initialize the Bloom filter with a given bit array size.
        
        :param size: The number of bits in the bit array.
        """
        self.size = size
        self.bit_array = bitarray.bitarray(size)
        self.bit_array.setall(0)

    def _hash1(self, url: str) -> int:
        """
        First hash function using a simple polynomial rolling hash.
        
        :param url: The URL to hash.
        :return: The hashed value mapped to the bit array size.
        """
        hash_value = 0
        prime = 31  # A prime number commonly used in hashing
        for char in url:
            hash_value = (hash_value * prime + ord(char)) % self.size
        return hash_value

    def _hash2(self, url: str) -> int:
        """
        Second hash function using the DJB2 algorithm.
        
        :param url: The URL to hash.
        :return: The hashed value mapped to the bit array size.
        """
        hash_value = 5381  # Initial value for DJB2
        for char in url:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)  # hash * 33 + char
        return hash_value % self.size

    def _hash3(self, url: str) -> int:
        """
        Third hash function using MD5.
        
        :param url: The URL to hash.
        :return: The hashed value mapped to the bit array size.
        """
        hash_value = 17
        for char in url:
            hash_value ^= (hash_value << 5) + (hash_value >> 2) + ord(char)
        return hash_value % self.size

class BloomFilterCaching:
    def __init__(self, size: int = 1000) -> None:
        """
        Initialize the Bloom filter with a given bit array size.
        
        :param size: The number of bits in the bit array.
        """
        self.bloom = BloomFilter(size=size)

    def add_url(self, url: str) -> None:
        """
        Add a URL to the Bloom filter.
        
        :param url: The URL to add.
        """
        for hash_func in [self.bloom._hash1, self.bloom._hash2, self.bloom._hash3]:
            self.bloom.bit_array[hash_func(url)] = 1

        write_output(f"Added: {url.strip()}")

    def check_url(self, url: str) -> bool:
        """
        Check if a URL is possibly in the Bloom filter.
        
        :param url: The URL to check.
        :return: True if the URL is possibly in the filter, False if definitely not.
        """
        exists_url = all(self.bloom.bit_array[hash_func(url)] for hash_func in [self.bloom._hash1, self.bloom._hash2, self.bloom._hash3])
        
        write_output(f"URL Existence Check for {url.strip()}: {exists_url}")

def initiateURLCaching(read_input_file: pathlib.Path) -> None:
    """
    Reads commands from the input file and processes them in the FlightReservation system.

    Args:
        read_input_file (pathlib.Path): Path to the input file.

    Output:
        None. Writes results of operations to the output file.
    """
    # Check if the provided input file exists; raise an error if not
    if not read_input_file.exists():
        raise Exception(f"Input file {read_input_file} does not exist")
    
    # Initialize the Bloom filter
    bloomFilterSystem = BloomFilterCaching(size=5000)  # Adjust size for lower false positives

    # Read commands from the input file and process them
    with open(read_input_file, 'r') as url_input:
        for command in url_input:
            operation, url_data = command.split(" ", 1)
            if re.match(r"(?i)^add*$", operation):
                bloomFilterSystem.add_url(url_data)
            elif re.match(r"(?i)^contains*$", operation):
                bloomFilterSystem.check_url(url_data)

if __name__ == "__main__":
    # Define the input file path & Initialize the flight reservation system
    read_input_file = pathlib.Path(__file__).parent / "inputPS03.txt"
    initiateURLCaching(read_input_file)
