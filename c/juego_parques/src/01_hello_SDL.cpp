#include <iostream>
#include <SDL2/SDL.h>

const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;

int main (int args, char* argv[])
{
	SDL_Window* window = NULL;
	SDL_Surface* screenSurface = NULL;
	
	if ( SDL_Init (SDL_INIT_VIDEO) < 0 )
	{
		std::cout << "Sdl could not initialize! Error " << SDL_GetError () << std::endl;
	}
	else
	{
		window = SDL_CreateWindow ("SDL Tutorial", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
		if ( window == NULL )
		{
			std::cout << "window could not be created! Error " << SDL_GetError () << std::endl; 
		}
		else
		{
			screenSurface = SDL_GetWindowSurface ( window );
			SDL_FillRect ( screenSurface, NULL, SDL_MapRGB ( screenSurface->format, 0xFF, 0xFF, 0xFF ) );
			SDL_UpdateWindowSurface ( window );
			SDL_Delay (2000);
		}
	}
	
	SDL_DestroyWindow ( window );
	SDL_Quit ();
	
	return 0;
}
