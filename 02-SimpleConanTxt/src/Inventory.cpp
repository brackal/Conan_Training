///////////////////////////////////////////////////////////
//  Inventory.cpp
//  Implementation of the Class Inventory
//  Created on:      13-Mrz-2026 16:02:42
//  Original author: aleksej.brack
///////////////////////////////////////////////////////////

#include "Inventory.h"


Inventory::Inventory(){
}


Inventory::~Inventory(){
}


void Inventory::AddGuitar(std::string serialNumber, 
						  float price, 
						  std::string builder, 
						  std::string model, 
						  std::string type, 
						  std::string backWood, 
						  std::string topWood){

	//guitars.push_back(Guitar(serialNumber, price, builder, model, type, backWood, topWood));

	Guitar* newGuitar = new Guitar(serialNumber, price, builder, model, type, backWood, topWood);

	guitars.push_back(*newGuitar);
}


Guitar Inventory::GetGuitar(std::string serialNumber){
	
	for(Guitar guitar : guitars){
		if(guitar.GetSerialNumber() == serialNumber){
			return guitar;
		}
	}
	return Guitar("", 0, "", "", "", "", ""); // Return a default-constructed Guitar object
}


Guitar Inventory::SearchGuitar(Guitar guitar){
	
	for(Guitar g : guitars){
		//Ignore serial number since that's unique
		//Ignore price since that's unique
		if(g.GetBuilder() == guitar.GetBuilder() &&
		   g.GetModel() == guitar.GetModel() &&
		   g.GetType() == guitar.GetType() &&
		   g.GetBackWood() == guitar.GetBackWood() &&
		   g.GetTopWood() == guitar.GetTopWood()){
			return g;
		}
	}
	
	return Guitar("", 0, "", "", "", "", ""); // Return a default-constructed Guitar object
}