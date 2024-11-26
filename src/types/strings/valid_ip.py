# https://www.geeksforgeeks.org/program-to-validate-an-ip-address/

# example: '172.16.254.1'


def is_valid_ip_address(ip_address_str: str) -> bool:
    if not ip_address_str:
        return False

    if ip_address_str.count(".") != 3:
        return False

    octets = ip_address_str.split(".")
    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit():
            return False

        octet_num = int(octet)
        if octet_num < 0 or octet_num > 255:
            return False

    return True


if __name__ == "__main__":
    input_ip_address = "172.16.254.1"
    print(f"{is_valid_ip_address(ip_address_str=input_ip_address)}")
