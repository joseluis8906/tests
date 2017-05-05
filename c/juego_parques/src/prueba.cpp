#include <iostream>
#include <SFML/Graphics.hpp>
#include <SFML/Audio.hpp>

int main ()
{
	sf::SoundBuffer buffer_sound;
	if (!buffer_sound.loadFromFile ("../sounds/dados.wav"))
	{
		std::cerr << "Error no se pudo cargar el track \"dados.wav\"." << std::endl;
	}
	
	sf::Sound dados;
	dados.setBuffer (buffer_sound);
	
	sf::Texture texture;
	if (!texture.loadFromFile ("../images/tablero.png"))
	{
		std::cerr << "Error no se pudo cargar la textura \"tablero.png\"." << std::endl;
	}

	texture.setSmooth (true);
	texture.setRepeated (false);
	
	sf::Sprite sprite1;
	sprite1.setTexture (texture);
	//sprite1.setTextureRect (sf::IntRect (0, 0, 1024, 593));
	sprite1.setPosition (sf::Vector2f (0, (720/2)-(sprite1.getLocalBounds().height/2)));

	sf::RenderWindow window (sf::VideoMode (1024, 720), "Parques");
	
	dados.play ();
	
	while (window.isOpen ()) 
	{
		sf::Event event;
		while (window.pollEvent (event));
		{
			if (event.type == sf::Event::Closed)
				window.close ();
		}
		
		window.clear (sf::Color::White);
		window.draw (sprite1);
		window.display ();
	}
	
	return 0;
}
