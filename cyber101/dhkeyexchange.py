# Diffie-Hellman Code

# Power function to return value of a^b mod P
def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

# Main function
def main():
    # Both persons agree upon the public keys G and P
    # A prime number P is taken
    P = 29
    print("The value of P:", P)

    # A primitive root for P, G is taken
    G = 5
    print("The value of G:", G)

    # Alice chooses the private key a
    # a is the chosen private key
    a = 12
    print("The private key a for Alice:", a)

    # Gets the generated key
    x = power(G, a, P)
    print("power mod is", x)

    # Bob chooses the private key b
    # b is the chosen private key
    b = 17
    print("The private key b for Bob:", b)

    # Gets the generated key
    y = power(G, b, P)

    print("second power mod is", y)

    # Generating the secret key after the exchange of keys
    ka = power(y, a, P)  # Secret key for Alice
    kb = power(x, b, P)  # Secret key for Bob

    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)

if __name__ == "__main__":
    main()
