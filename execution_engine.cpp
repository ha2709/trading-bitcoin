#include <iostream>
#include <string>
#include <chrono>
#include <thread>  // Include this for std::this_thread

// A simple Order class that could be expanded with more details
class Order {
public:
    enum class Type { BUY, SELL } type;
    std::string symbol;
    int quantity;
    double price;
    // Timestamp to track latency
    std::chrono::high_resolution_clock::time_point timestamp;

    Order(Type type, std::string symbol, int quantity, double price)
        : type(type), symbol(symbol), quantity(quantity), price(price) {
        timestamp = std::chrono::high_resolution_clock::now();
    }

    // Method to execute the order, in reality, this would interface with an exchange's API
    void execute() {
        auto now = std::chrono::high_resolution_clock::now();
        auto latency = std::chrono::duration_cast<std::chrono::microseconds>(now - timestamp).count();
        std::cout << "Executing " << (type == Type::BUY ? "Buy" : "Sell")
                  << " order for " << quantity << " shares of " << symbol
                  << " at $" << price << ", latency: " << latency << " microseconds.\n";
        // In a real system, API calls to the broker/exchange would go here
    }
};

// A mock function that simulates order execution with a delay to mimic network latency
void simulate_order_execution(Order& order) {
    // Simulating network and processing delay
    std::this_thread::sleep_for(std::chrono::milliseconds(1));
    order.execute();
}

int main() {
    // Example usage:
    Order buyOrder(Order::Type::BUY, "AAPL", 100, 150.00);
    simulate_order_execution(buyOrder);

    Order sellOrder(Order::Type::SELL, "GOOGL", 50, 2750.00);
    simulate_order_execution(sellOrder);

    return 0;
}
