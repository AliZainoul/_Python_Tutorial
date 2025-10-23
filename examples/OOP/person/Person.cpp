#include <iostream>
using namespace std;
class Person {
    private: string name; 
    public: Person(string n) : name(n) {}
    
    string getName() { return name; }
};

int main() { 
    Person p("Alice"); 
    cout << p.name << endl; 
    p.name = "Ali";
    cout << p.name << endl; 

    return 0; 
}


/*
(base) 💻 ~/_Python_Tutorial/examples/OOP % g++ Person.cpp -o Person && ./Person

Person.cpp:12:15: error: 'name' is a private member of 'Person'
    cout << p.name << endl;
              ^
Person.cpp:4:21: note: declared private here
    private: string name;
                    ^
Person.cpp:13:7: error: 'name' is a private member of 'Person'
    p.name = "Ali";
      ^
Person.cpp:4:21: note: declared private here
    private: string name;
                    ^
Person.cpp:14:15: error: 'name' is a private member of 'Person'
    cout << p.name << endl;
              ^
Person.cpp:4:21: note: declared private here
    private: string name;
                    ^
3 errors generated.
(base) 💻 ~/_Python_Tutorial/examples/OOP %
*/