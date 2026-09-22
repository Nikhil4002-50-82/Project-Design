// Task 1 - Create the entry file and print welcome header
// Step 1: Entry File Setup
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Converter {

    // Step 2: Welcome Banner Output
    static void printWelcome() {
        System.out.println("Welcome to Multi-Unit & Currency Converter CLI!");
    }

    // Task 2 - Define Currency rates table (Base: USD)
    // Step 1: Declare Currency Rates Lookup Table
    static final Map<String, Double> CURRENCY_RATES = new HashMap<>();
    static {
        CURRENCY_RATES.put("USD", 1.0);
        CURRENCY_RATES.put("EUR", 0.92);
        CURRENCY_RATES.put("GBP", 0.79);
        CURRENCY_RATES.put("INR", 83.0);
        CURRENCY_RATES.put("JPY", 155.0);
        CURRENCY_RATES.put("CAD", 1.36);
    }

    // Task 3 - Implement Currency conversion function
    static double convertCurrency(double amount, String fromUnit, String toUnit) {
        // Step 1: Pivot Input Amount to Standard Base (USD)
        double amountInUsd = amount / CURRENCY_RATES.get(fromUnit);

        // Step 2: Project Base Amount to Target Currency
        return amountInUsd * CURRENCY_RATES.get(toUnit);
    }

    // Task 4 - Define Length conversion ratios (Base: Meters)
    // Step 1: Declare Length Ratios Lookup Table
    static final Map<String, Double> LENGTH_RATIOS = new HashMap<>();
    static {
        LENGTH_RATIOS.put("m", 1.0);
        LENGTH_RATIOS.put("km", 1000.0);
        LENGTH_RATIOS.put("mi", 1609.344);
        LENGTH_RATIOS.put("ft", 0.3048);
        LENGTH_RATIOS.put("in", 0.0254);
    }

    // Task 5 - Implement Length conversion function
    static double convertLength(double amount, String fromUnit, String toUnit) {
        // Step 1: Normalize Distance to Base Metric (Meters)
        double amountInMeters = amount * LENGTH_RATIOS.get(fromUnit);

        // Step 2: Project Base Distance to Target Unit
        return amountInMeters / LENGTH_RATIOS.get(toUnit);
    }

    // Task 6 - Define Weight conversion ratios (Base: Kilograms)
    // Step 1: Declare Weight Ratios Lookup Table
    static final Map<String, Double> WEIGHT_RATIOS = new HashMap<>();
    static {
        WEIGHT_RATIOS.put("kg", 1.0);
        WEIGHT_RATIOS.put("g", 0.001);
        WEIGHT_RATIOS.put("lbs", 0.45359237);
        WEIGHT_RATIOS.put("oz", 0.028349523125);
    }

    // Task 7 - Implement Weight conversion function
    static double convertWeight(double amount, String fromUnit, String toUnit) {
        // Step 1: Normalize Mass to Base Metric (Kilograms)
        double amountInKg = amount * WEIGHT_RATIOS.get(fromUnit);

        // Step 2: Project Base Mass to Target Unit
        return amountInKg / WEIGHT_RATIOS.get(toUnit);
    }

    // Task 8 - Implement Temperature conversion function (Base: Celsius)
    static boolean isBelowAbsoluteZero(double amount, String unit) {
        // Step 1: Validate Absolute Zero Physical Boundary
        if (unit.equals("C") && amount < -273.15) return true;
        if (unit.equals("F") && amount < -459.67) return true;
        if (unit.equals("K") && amount < 0.0) return true;
        return false;
    }

    static double convertTemperature(double amount, String fromUnit, String toUnit) {
        // Step 2: Convert Input Scale to Base Celsius
        double celsius = 0.0;
        if (fromUnit.equals("C")) {
            celsius = amount;
        } else if (fromUnit.equals("F")) {
            celsius = (amount - 32.0) * 5.0 / 9.0;
        } else if (fromUnit.equals("K")) {
            celsius = amount - 273.15;
        }

        // Step 3: Project Base Celsius to Target Scale
        if (toUnit.equals("C")) {
            return celsius;
        } else if (toUnit.equals("F")) {
            return (celsius * 9.0 / 5.0) + 32.0;
        } else if (toUnit.equals("K")) {
            return celsius + 273.15;
        }
        return 0.0;
    }

    // Task 9 - Validate numeric input
    static double getPositiveNumber(Scanner scanner, String prompt) {
        // Step 1: Read and Validate Non-Negative Number
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine().trim();
            try {
                double val = Double.parseDouble(input);
                if (val < 0.0) {
                    System.out.println("Error: Amount cannot be negative. Please enter a positive value.");
                    continue;
                }
                return val;
            } catch (NumberFormatException e) {
                System.out.println("Error: Invalid numeric input. Please enter a valid number.");
            }
        }
    }

    static double getTemperatureNumber(Scanner scanner, String prompt, String unit) {
        // Step 2: Read and Validate Bounded Temperature
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine().trim();
            try {
                double val = Double.parseDouble(input);
                if (isBelowAbsoluteZero(val, unit)) {
                    System.out.println("Error: Temperature cannot be below Absolute Zero (" + val + " " + unit + ").");
                    continue;
                }
                return val;
            } catch (NumberFormatException e) {
                System.out.println("Error: Invalid numeric input. Please enter a valid number.");
            }
        }
    }

    // Task 10 - Validate unit selections
    static String getValidUnit(Scanner scanner, String prompt, List<String> allowedUnits) {
        // Step 1: Normalize Case and Match Against Allowed Units
        while (true) {
            System.out.print(prompt);
            String input = scanner.nextLine().trim();
            for (String original : allowedUnits) {
                if (input.equalsIgnoreCase(original)) {
                    return original;
                }
            }
            System.out.println("Error: Invalid unit '" + input + "'. Allowed options: " + String.join(", ", allowedUnits));
        }
    }

    // Task 11 - Build interactive conversion handlers
    static void handleCurrency(Scanner scanner) {
        // Step 1: Build Currency Conversion Handler
        System.out.println("\n--- CURRENCY CONVERTER ---");
        List<String> units = Arrays.asList("USD", "EUR", "GBP", "INR", "JPY", "CAD");
        System.out.println("Supported Currencies: " + String.join(", ", units));

        String fromCurr = getValidUnit(scanner, "Enter Source Currency: ", units);
        String toCurr = getValidUnit(scanner, "Enter Target Currency: ", units);
        double amount = getPositiveNumber(scanner, "Enter amount in " + fromCurr + ": ");

        double result = convertCurrency(amount, fromCurr, toCurr);
        double rate = convertCurrency(1.0, fromCurr, toCurr);

        System.out.printf("\n>> RESULT: %.2f %s = %.2f %s%n", amount, fromCurr, result, toCurr);
        System.out.printf("   (Exchange Rate: 1 %s = %.4f %s)%n", fromCurr, rate, toCurr);
    }

    static void handleLength(Scanner scanner) {
        // Step 2: Build Length Conversion Handler
        System.out.println("\n--- LENGTH CONVERTER ---");
        List<String> units = Arrays.asList("m", "km", "mi", "ft", "in");
        System.out.println("Supported Units: " + String.join(", ", units) + " (m=meters, km=kilometers, mi=miles, ft=feet, in=inches)");

        String fromU = getValidUnit(scanner, "Enter Source Unit: ", units);
        String toU = getValidUnit(scanner, "Enter Target Unit: ", units);
        double amount = getPositiveNumber(scanner, "Enter distance in " + fromU + ": ");

        double result = convertLength(amount, fromU, toU);
        double rate = convertLength(1.0, fromU, toU);

        System.out.printf("\n>> RESULT: %.4f %s = %.4f %s%n", amount, fromU, result, toU);
        System.out.printf("   (Ratio: 1 %s = %.4f %s)%n", fromU, rate, toU);
    }

    static void handleWeight(Scanner scanner) {
        // Step 3: Build Weight Conversion Handler
        System.out.println("\n--- WEIGHT CONVERTER ---");
        List<String> units = Arrays.asList("kg", "g", "lbs", "oz");
        System.out.println("Supported Units: " + String.join(", ", units) + " (kg=kilograms, g=grams, lbs=pounds, oz=ounces)");

        String fromU = getValidUnit(scanner, "Enter Source Unit: ", units);
        String toU = getValidUnit(scanner, "Enter Target Unit: ", units);
        double amount = getPositiveNumber(scanner, "Enter weight in " + fromU + ": ");

        double result = convertWeight(amount, fromU, toU);
        double rate = convertWeight(1.0, fromU, toU);

        System.out.printf("\n>> RESULT: %.4f %s = %.4f %s%n", amount, fromU, result, toU);
        System.out.printf("   (Ratio: 1 %s = %.4f %s)%n", fromU, rate, toU);
    }

    static void handleTemperature(Scanner scanner) {
        // Step 4: Build Temperature Conversion Handler
        System.out.println("\n--- TEMPERATURE CONVERTER ---");
        List<String> units = Arrays.asList("C", "F", "K");
        System.out.println("Supported Scales: " + String.join(", ", units) + " (C=Celsius, F=Fahrenheit, K=Kelvin)");

        String fromU = getValidUnit(scanner, "Enter Source Scale: ", units);
        String toU = getValidUnit(scanner, "Enter Target Scale: ", units);
        double amount = getTemperatureNumber(scanner, "Enter temperature in " + fromU + ": ", fromU);

        double result = convertTemperature(amount, fromU, toU);

        System.out.printf("\n>> RESULT: %.2f %s = %.2f %s%n", amount, fromU, result, toU);
    }

    // Task 12 - Implement main menu loop and application assembly
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Step 4: Assemble Main Entry Point Guard
        printWelcome();

        while (true) {
            // Step 1: Render Interactive Menu Banner
            System.out.println("\n========================================");
            System.out.println("   MULTI-UNIT & CURRENCY CONVERTER CLI   ");
            System.out.println("========================================");
            System.out.println("1. Currency Converter (USD, EUR, GBP, INR, JPY, CAD)");
            System.out.println("2. Length Converter (m, km, mi, ft, in)");
            System.out.println("3. Weight Converter (kg, g, lbs, oz)");
            System.out.println("4. Temperature Converter (C, F, K)");
            System.out.println("5. Exit");
            System.out.println("----------------------------------------");
            System.out.print("Enter your choice (1-5): ");

            // Step 2: Prompt and Route User Selection
            String choice = scanner.nextLine().trim();

            if (choice.equals("1")) {
                handleCurrency(scanner);
            } else if (choice.equals("2")) {
                handleLength(scanner);
            } else if (choice.equals("3")) {
                handleWeight(scanner);
            } else if (choice.equals("4")) {
                handleTemperature(scanner);
            } else if (choice.equals("5")) {
                // Step 3: Handle Exit and Farewell
                System.out.println("\nThank you for using Multi-Unit & Currency Converter CLI. Goodbye!");
                break;
            } else {
                System.out.println("Invalid choice. Please enter a number between 1 and 5.");
            }
        }

        scanner.close();
    }
}
