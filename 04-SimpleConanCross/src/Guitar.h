///////////////////////////////////////////////////////////
//  Guitar.h
//  Implementation of the Class Guitar
//  Created on:      13-Mrz-2026 16:02:42
//  Original author: aleksej.brack
///////////////////////////////////////////////////////////


#if !defined(EA_282813A7_E0DA_49b4_9273_C1A966803836__INCLUDED_)
#define EA_282813A7_E0DA_49b4_9273_C1A966803836__INCLUDED_

#include <string>

class Guitar
{

public:
	Guitar(std::string serialNumber, 
		float price, 
		std::string builder, 
		std::string model, 
		std::string type, 
		std::string backWood, 
		std::string topWood);

	virtual ~Guitar();

	std::string GetSerialNumber();
	float GetPrice();
	void SetPrice(float prise);
	std::string GetBuilder();
	std::string GetModel();
	std::string GetType();
	std::string GetBackWood();
	std::string GetTopWood();

private:
	std::string serialNumber;
	float price;
	std::string builder;
	std::string model;
	std::string type;
	std::string backWood;
	std::string topWood;

};
#endif // !defined(EA_282813A7_E0DA_49b4_9273_C1A966803836__INCLUDED_)
