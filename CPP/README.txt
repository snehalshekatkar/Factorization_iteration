primesieve 3.6
April 23, 2012
Kim Walisch, <kim.walisch@gmail.com>

About primesieve
================

primesieve is a free software program that generates prime numbers and
prime k-tuplets (twin primes, prime triplets, ...) < 2^64 using a
highly optimized implementation of the sieve of Eratosthenes.

Homepage: http://primesieve.googlecode.com

New in version 3.6
==================

+ Built with Intel C++ Compiler 12.1 (Composer XE 2011)
+ Minor speed up for small sieving primes ~ 5%

Complete changelog:
http://primesieve.googlecode.com/source/browse/tags/primesieve-3.6/docs/CHANGES

Usage
=====

By default primesieve counts prime numbers to print the primes choose
'Print->Prime numbers' from the menu.
The best sieving performance is achieved with a sieve size of the
CPU's L1 data cache size (usually 32 or 64 KB) when sieving < 10^16
and a sieve size of the CPU's L2 cache size above.

License
=======

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
