import hashlib

# 64KBs chunks
SHA256_BUFF_SIZE = 65536


def calculate_sha256(content: bytes):
    """
    Efficiently calculate the SHA1 hash for a file.

    :param file_path:
    :return:
    """

    sha256 = hashlib.sha256()

    index = 0
    while index < len(content):
        chunk = content[index:index + SHA256_BUFF_SIZE]
        sha256.update(chunk)
        index += SHA256_BUFF_SIZE
    return sha256.hexdigest()