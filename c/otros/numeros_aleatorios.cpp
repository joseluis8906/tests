#include <iostream>
#include <random>
#include <ctime>
#include <iomanip>

int main (int argc, char *argv[])
{
	std::time_t seed;
	std::time (&seed);
	
	std::default_random_engine random_engine(seed);
	std::uniform_real_distribution<float> float_distribution (5.00, 39.42);
	
	for (int i=0; i<100; i++)
	{
		std::cout << std::setprecision(4) << float_distribution (random_engine);
		(((i+1)%10)==0) ? std::cout << std::endl : std::cout << ",";
	}
	return 0;
}
