#include <iostream>
#include <SDL2/SDL.h>

int main (int args, char* argv[])
{
	if (SDL_Init(SDL_INIT_EVERYTHING) != 0)
	{
		std::cout << "Sdl init error: " << SDL_GetError () << std::endl;
		return 1;
	}
	
	SDL_Quit ();
	
	return 0;
}
