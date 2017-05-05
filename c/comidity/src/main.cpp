#include <iostream>
#include <vector>
#include <SFML/Graphics.hpp>

int main ()
{
    /*std::vector<sf::VideoMode> modes = sf::VideoMode::getFullscreenModes();
    for (std::size_t i = 0; i < modes.size (); ++i)
    {
        sf::VideoMode mode = modes[i];
        std::cout << "Mode #" << i << ": " << mode.width << "x" << mode.height << " - " << mode.bitsPerPixel << " bpp" << std::endl;
    }*/
    sf::VideoMode desktop = sf::VideoMode::getDesktopMode ();
    sf::RenderWindow window (desktop, "Comidity");
    
    sf::CircleShape shape (48.f);
    shape.setFillColor (sf::Color::Green);
    
    while (window.isOpen ())
    {
        sf::Event event;
        while (window.pollEvent (event))
        {
            if (event.type == sf::Event::Closed)
            {
                window.close ();
            }
        }
        
        window.clear ();
        window.draw (shape);
        window.display ();
    }
    
    return 0;
}
