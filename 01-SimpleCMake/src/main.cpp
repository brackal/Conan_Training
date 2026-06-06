// Hier beginnt und endet die Ausführung des Programms.
//

#include <iostream>
//#include <fmt/core.h>
#include "Guitar.h"
#include "Inventory.h"


int main()
{

  std::cout << "Hello World!" << std::endl;

  // fmt verwenden
  //fmt::print("Hallo von fmt!\n");


  Inventory inventory;
  inventory.AddGuitar("V95693", 1499.95, "Fender", "Stratocastor", "Electric", "Alder", "Alder");
  inventory.AddGuitar("V9512", 1549.95, "Fender", "Stratocastor", "Electric", "Alder", "Alder");
  inventory.AddGuitar("122784", 5495.95, "Martin", "D-18", "Acoustic", "Mahogany", "Adirondack");
  inventory.AddGuitar("76531", 6295.95, "Martin", "OM-28", "Acoustic", "Rosewood", "Adirondack");
  inventory.AddGuitar("70108276", 2295.95, "Gibson", "Les Paul", "Electric", "Mahogany", "Mahogany");
  inventory.AddGuitar("82765501", 1890.95, "Gibson", "SG '61 Reissue", "Electric", "Mahogany", "Mahogany");
  
  Guitar whatErinLikes = Guitar("", 0, "fender", "Stratocastor", "Electric", "Alder", "Alder");
  Guitar guitar = inventory.SearchGuitar(whatErinLikes);

  if (guitar.GetSerialNumber() != "") {
    std::cout << "Erin is looking for a " << whatErinLikes.GetBuilder() << " " << whatErinLikes.GetModel() << " " << whatErinLikes.GetType() << "." << std::endl;
    std::cout << "Found guitar: " << guitar.GetSerialNumber() << std::endl;
  } else {
    std::cout << "Sorry, Erin, we have nothing for you." << std::endl;
  }


  while(true) {
    // Infinite loop to keep the program running
  }
  return 0;
}
