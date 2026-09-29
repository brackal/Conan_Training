///////////////////////////////////////////////////////////
//  Inventory.h
//  Implementation of the Class Inventory
//  Created on:      13-Mrz-2026 16:02:42
//  Original author: aleksej.brack
///////////////////////////////////////////////////////////

#if !defined(EA_42C4849D_1FFA_408f_BBD0_89463824A1A1__INCLUDED_)
#define EA_42C4849D_1FFA_408f_BBD0_89463824A1A1__INCLUDED_

#include <string>
#include <list>
#include "Guitar.h"

class Inventory
{

public:
	Inventory();
	virtual ~Inventory();

	void AddGuitar(std::string serialNumber, 
		float price, 
		std::string builder, 
		std::string model, 
		std::string type, 
		std::string backWood, 
		std::string topWood);
	Guitar GetGuitar(std::string serialNumber);
	Guitar SearchGuitar(Guitar guitar);

	private:
	std::list <Guitar> guitars;

};
#endif // !defined(EA_42C4849D_1FFA_408f_BBD0_89463824A1A1__INCLUDED_)
