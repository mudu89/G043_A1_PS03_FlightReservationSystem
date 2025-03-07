import pathlib
import re
from typing import Optional
import mmh3  # MurmurHash for fast non-cryptographic hashing
import hashlib  # For SHA-256 and MD5
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

class BloomFilterCaching:
    def __init__(self, size: int = 1000) -> None:
        """
        Initialize the Bloom filter with a given bit array size.
        
        :param size: The number of bits in the bit array.
        """
        self.bloom = BloomFilter(size=size)

    def _hash1(self, url: str) -> int:
        """
        First hash function using MurmurHash.
        
        :param url: The URL to hash.
        :return: The hashed value mapped to the bit array size.
        """
        return mmh3.hash(url, 42) % self.bloom.size  # 42 is a random seed

    def _hash2(self, url: str) -> int:
        """
        Second hash function using SHA-256.
        
        :param url: The URL to hash.
        :return: The hashed value mapped to the bit array size.
        """
        return int(hashlib.sha256(url.encode()).hexdigest(), 16) % self.bloom.size

    def _hash3(self, url: str) -> int:
        """
        Third hash function using MD5.
        
        :param url: The URL to hash.
        :return: The hashed value mapped to the bit array size.
        """
        return int(hashlib.md5(url.encode()).hexdigest(), 16) % self.bloom.size

    def add_url(self, url: str) -> None:
        """
        Add a URL to the Bloom filter.
        
        :param url: The URL to add.
        """
        self.bloom.bit_array[self._hash1(url)] = 1
        self.bloom.bit_array[self._hash2(url)] = 1
        self.bloom.bit_array[self._hash3(url)] = 1

        write_output(f"Added: {url.strip()}")

    def check_url(self, url: str) -> bool:
        """
        Check if a URL is possibly in the Bloom filter.
        
        :param url: The URL to check.
        :return: True if the URL is possibly in the filter, False if definitely not.
        """
        exists_url =  (self.bloom.bit_array[self._hash1(url)] and 
                self.bloom.bit_array[self._hash2(url)] and 
                self.bloom.bit_array[self._hash3(url)])
        if exists_url:
            write_output(f"URL Existence Check for {url.strip()}: True")
        else:
            write_output(f"URL Existence Check for {url.strip()}: False")

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
            print(f"Operation: {operation}, URL: {url_data}")
            if re.match(r"(?i)^add*$", operation):
                print("Adding URL")
                bloomFilterSystem.add_url(url_data)
            elif re.match(r"(?i)^contains*$", operation):
                bloomFilterSystem.check_url(url_data)

if __name__ == "__main__":
    # Define the input file path & Initialize the flight reservation system
    read_input_file = pathlib.Path(__file__).parent / "inputPS03.txt"
    print(f"Reading input from: {read_input_file}")
    initiateURLCaching(read_input_file)