///////////////////////////////////////////////////////////
//  Guitar.cpp
//  Implementation of the Class Guitar
//  Created on:      13-Mrz-2026 16:02:42
//  Original author: aleksej.brack
///////////////////////////////////////////////////////////

#include "Guitar.h"


Guitar::Guitar(std::string serialNumber, 
		float price, 
		std::string builder, 
		std::string model, 
		std::string type, 
		std::string backWood, 
		std::string topWood) : serialNumber(serialNumber), 
								price(price), 
								builder(builder), 
								model(model), 
								type(type), 
								backWood(backWood), 
								topWood(topWood) {
}

Guitar::~Guitar(){
}



std::string Guitar::GetSerialNumber(){
	return  serialNumber;
}


float Guitar::GetPrice(){
	return  price;
}


void Guitar::SetPrice(float prise){
	this->price = prise;
}


std::string Guitar::GetBuilder(){
	return  builder;
}


std::string Guitar::GetModel(){
	return  model;
}


std::string Guitar::GetType(){
	return  type;
}


std::string Guitar::GetBackWood(){
	return  backWood;
}


std::string Guitar::GetTopWood(){
	return  topWood;
}