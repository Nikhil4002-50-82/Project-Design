// Task 1 - Create the entry file and print welcome header
// Step 1: Entry File Setup
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <iomanip>
#include <cctype>
#include <stdexcept>

using namespace std;

// Helper to convert string to lowercase
string toLowerStr(const string& s) {
    string res = "";
    for (char c : s) {
        res += static_cast<char>(tolower(static_cast<unsigned char>(c)));
    }
    return res;
}

// Helper to trim leading/trailing whitespace only
string trimStr(const string& s) {
    size_t start = s.find_first_not_of(" \t\r\n");
    size_t end = s.find_last_not_of(" \t\r\n");
    if (start == string::npos) {
        return "";
    }
    return s.substr(start, end - start + 1);
}

// Step 2: Welcome Banner Output
void printWelcome() {
    cout << "Welcome to Multi-Unit & Currency Converter CLI!\n";
}

// Task 2 - Define Currency rates table (Base: USD)
// Step 1: Declare Currency Rates Lookup Table
const map<string, double> CURRENCY_RATES = {
    {"USD", 1.0},
    {"EUR", 0.92},
    {"GBP", 0.79},
    {"INR", 83.0},
    {"JPY", 155.0},
    {"CAD", 1.36}
};

// Task 3 - Implement Currency conversion function
double convertCurrency(double amount, const string& fromUnit, const string& toUnit) {
    // Step 1: Pivot Input Amount to Standard Base (USD)
    double amountInUsd = amount / CURRENCY_RATES.at(fromUnit);

    // Step 2: Project Base Amount to Target Currency
    return amountInUsd * CURRENCY_RATES.at(toUnit);
}

// Task 4 - Define Length conversion ratios (Base: Meters)
// Step 1: Declare Length Ratios Lookup Table
const map<string, double> LENGTH_RATIOS = {
    {"m", 1.0},
    {"km", 1000.0},
    {"mi", 1609.344},
    {"ft", 0.3048},
    {"in", 0.0254}
};

// Task 5 - Implement Length conversion function
double convertLength(double amount, const string& fromUnit, const string& toUnit) {
    // Step 1: Normalize Distance to Base Metric (Meters)
    double amountInMeters = amount * LENGTH_RATIOS.at(fromUnit);

    // Step 2: Project Base Distance to Target Unit
    return amountInMeters / LENGTH_RATIOS.at(toUnit);
}

// Task 6 - Define Weight conversion ratios (Base: Kilograms)
// Step 1: Declare Weight Ratios Lookup Table
const map<string, double> WEIGHT_RATIOS = {
    {"kg", 1.0},
    {"g", 0.001},
    {"lbs", 0.45359237},
    {"oz", 0.028349523125}
};

// Task 7 - Implement Weight conversion function
double convertWeight(double amount, const string& fromUnit, const string& toUnit) {
    // Step 1: Normalize Mass to Base Metric (Kilograms)
    double amountInKg = amount * WEIGHT_RATIOS.at(fromUnit);

    // Step 2: Project Base Mass to Target Unit
    return amountInKg / WEIGHT_RATIOS.at(toUnit);
}

// Task 8 - Implement Temperature conversion function (Base: Celsius)
bool isBelowAbsoluteZero(double amount, const string& unit) {
    // Step 1: Validate Absolute Zero Physical Boundary
    if (unit == "C" && amount < -273.15) return true;
    if (unit == "F" && amount < -459.67) return true;
    if (unit == "K" && amount < 0.0) return true;
    return false;
}

double convertTemperature(double amount, const string& fromUnit, const string& toUnit) {
    // Step 2: Convert Input Scale to Base Celsius
    double celsius = 0.0;
    if (fromUnit == "C") {
        celsius = amount;
    } else if (fromUnit == "F") {
        celsius = (amount - 32.0) * 5.0 / 9.0;
    } else if (fromUnit == "K") {
        celsius = amount - 273.15;
    }

    // Step 3: Project Base Celsius to Target Scale
    if (toUnit == "C") {
        return celsius;
    } else if (toUnit == "F") {
        return (celsius * 9.0 / 5.0) + 32.0;
    } else if (toUnit == "K") {
        return celsius + 273.15;
    }
    return 0.0;
}

// Task 9 - Validate numeric input
double getPositiveNumber(const string& prompt) {
    // Step 1: Read and Validate Non-Negative Number
    while (true) {
        cout << prompt;
        string input;
        getline(cin, input);
        input = trimStr(input);
        try {
            size_t idx;
            double val = stod(input, &idx);
            if (idx != input.length()) {
                cout << "Error: Invalid numeric input. Please enter a valid number.\n";
                continue;
            }
            if (val < 0.0) {
                cout << "Error: Amount cannot be negative. Please enter a positive value.\n";
                continue;
            }
            return val;
        } catch (const exception& e) {
            cout << "Error: Invalid numeric input. Please enter a valid number.\n";
        }
    }
}

double getTemperatureNumber(const string& prompt, const string& unit) {
    // Step 2: Read and Validate Bounded Temperature
    while (true) {
        cout << prompt;
        string input;
        getline(cin, input);
        input = trimStr(input);
        try {
            size_t idx;
            double val = stod(input, &idx);
            if (idx != input.length()) {
                cout << "Error: Invalid numeric input. Please enter a valid number.\n";
                continue;
            }
            if (isBelowAbsoluteZero(val, unit)) {
                cout << "Error: Temperature cannot be below Absolute Zero (" << val << " " << unit << ").\n";
                continue;
            }
            return val;
        } catch (const exception& e) {
            cout << "Error: Invalid numeric input. Please enter a valid number.\n";
        }
    }
}

// Task 10 - Validate unit selections
string getValidUnit(const string& prompt, const vector<string>& allowedUnits) {
    // Step 1: Normalize Case and Match Against Allowed Units
    while (true) {
        cout << prompt;
        string input;
        getline(cin, input);

        string cleaned = trimStr(input);

        for (const string& original : allowedUnits) {
            if (toLowerStr(cleaned) == toLowerStr(original)) {
                return original;
            }
        }

        cout << "Error: Invalid unit '" << input << "'. Allowed options: ";
        for (size_t i = 0; i < allowedUnits.size(); ++i) {
            cout << allowedUnits[i] << (i + 1 < allowedUnits.size() ? ", " : "\n");
        }
    }
}

// Task 11 - Build interactive conversion handlers
void handleCurrency() {
    // Step 1: Build Currency Conversion Handler
    cout << "\n--- CURRENCY CONVERTER ---\n";
    vector<string> units = {"USD", "EUR", "GBP", "INR", "JPY", "CAD"};
    cout << "Supported Currencies: USD, EUR, GBP, INR, JPY, CAD\n";

    string fromCurr = getValidUnit("Enter Source Currency: ", units);
    string toCurr = getValidUnit("Enter Target Currency: ", units);
    double amount = getPositiveNumber("Enter amount in " + fromCurr + ": ");

    double result = convertCurrency(amount, fromCurr, toCurr);
    double rate = convertCurrency(1.0, fromCurr, toCurr);

    cout << fixed << setprecision(2);
    cout << "\n>> RESULT: " << amount << " " << fromCurr << " = " << result << " " << toCurr << "\n";
    cout << fixed << setprecision(4);
    cout << "   (Exchange Rate: 1 " << fromCurr << " = " << rate << " " << toCurr << ")\n";
}

void handleLength() {
    // Step 2: Build Length Conversion Handler
    cout << "\n--- LENGTH CONVERTER ---\n";
    vector<string> units = {"m", "km", "mi", "ft", "in"};
    cout << "Supported Units: m, km, mi, ft, in (m=meters, km=kilometers, mi=miles, ft=feet, in=inches)\n";

    string fromU = getValidUnit("Enter Source Unit: ", units);
    string toU = getValidUnit("Enter Target Unit: ", units);
    double amount = getPositiveNumber("Enter distance in " + fromU + ": ");

    double result = convertLength(amount, fromU, toU);
    double rate = convertLength(1.0, fromU, toU);

    cout << fixed << setprecision(4);
    cout << "\n>> RESULT: " << amount << " " << fromU << " = " << result << " " << toU << "\n";
    cout << "   (Ratio: 1 " << fromU << " = " << rate << " " << toU << ")\n";
}

void handleWeight() {
    // Step 3: Build Weight Conversion Handler
    cout << "\n--- WEIGHT CONVERTER ---\n";
    vector<string> units = {"kg", "g", "lbs", "oz"};
    cout << "Supported Units: kg, g, lbs, oz (kg=kilograms, g=grams, lbs=pounds, oz=ounces)\n";

    string fromU = getValidUnit("Enter Source Unit: ", units);
    string toU = getValidUnit("Enter Target Unit: ", units);
    double amount = getPositiveNumber("Enter weight in " + fromU + ": ");

    double result = convertWeight(amount, fromU, toU);
    double rate = convertWeight(1.0, fromU, toU);

    cout << fixed << setprecision(4);
    cout << "\n>> RESULT: " << amount << " " << fromU << " = " << result << " " << toU << "\n";
    cout << "   (Ratio: 1 " << fromU << " = " << rate << " " << toU << ")\n";
}

void handleTemperature() {
    // Step 4: Build Temperature Conversion Handler
    cout << "\n--- TEMPERATURE CONVERTER ---\n";
    vector<string> units = {"C", "F", "K"};
    cout << "Supported Scales: C, F, K (C=Celsius, F=Fahrenheit, K=Kelvin)\n";

    string fromU = getValidUnit("Enter Source Scale: ", units);
    string toU = getValidUnit("Enter Target Scale: ", units);
    double amount = getTemperatureNumber("Enter temperature in " + fromU + ": ", fromU);

    double result = convertTemperature(amount, fromU, toU);

    cout << fixed << setprecision(2);
    cout << "\n>> RESULT: " << amount << " " << fromU << " = " << result << " " << toU << "\n";
}

// Task 12 - Implement main menu loop and application assembly
int main() {
    // Step 4: Assemble Main Entry Point Guard
    printWelcome();

    while (true) {
        // Step 1: Render Interactive Menu Banner
        cout << "\n========================================\n";
        cout << "   MULTI-UNIT & CURRENCY CONVERTER CLI   \n";
        cout << "========================================\n";
        cout << "1. Currency Converter (USD, EUR, GBP, INR, JPY, CAD)\n";
        cout << "2. Length Converter (m, km, mi, ft, in)\n";
        cout << "3. Weight Converter (kg, g, lbs, oz)\n";
        cout << "4. Temperature Converter (C, F, K)\n";
        cout << "5. Exit\n";
        cout << "----------------------------------------\n";
        cout << "Enter your choice (1-5): ";

        // Step 2: Prompt and Route User Selection
        string choice;
        getline(cin, choice);

        string cleaned = trimStr(choice);

        if (cleaned == "1") {
            handleCurrency();
        } else if (cleaned == "2") {
            handleLength();
        } else if (cleaned == "3") {
            handleWeight();
        } else if (cleaned == "4") {
            handleTemperature();
        } else if (cleaned == "5") {
            // Step 3: Handle Exit and Farewell
            cout << "\nThank you for using Multi-Unit & Currency Converter CLI. Goodbye!\n";
            break;
        } else {
            cout << "Invalid choice. Please enter a number between 1 and 5.\n";
        }
    }
    return 0;
}
