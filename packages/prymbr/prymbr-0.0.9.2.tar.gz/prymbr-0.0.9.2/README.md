# prymbr

A Package to simplify the usage of prime numbers, fractions, and other simple yet time consuming operations.

### Features:
+ Check if a number is prime
+ Decompose a number into a sequence of prime factors
+ Find gcd and lcm of 2 numbers
+ Create fractions
+ Simplify fractions to the maximum
+ Convert fractions back to decimals
+ And more!

### Incoming Update:
+ Faster calculations with the use of [Simd](https://pypi.org/project/simd/) library
+ More calculation options

### Usage:

Install `prymbr` on your system with pip:

```
pip install prymbr
```

### Example:

```python
import prymbr

print(prymbr.isprime(51)) #False

print(prymbr.decomp(78)) #[2, 3, 13]

print(prymbr.pgcd(45, 63)) #7
print(prymbr.gcd(45, 63)) #7

print(prymbr.ppcm(45, 63)) #405
print(prymbr.lcm(45, 63)) #405

fraction = prymbr.frac(88, 48) #88/48
print(fraction)

print(prymbr.simp(fraction)) #11/6

print(prymbr.deci(fraction)) #1.8333

print(prymbr.frac(fraction)) #True

print(prymbr.frac(1.6424)) #2053/1250
```