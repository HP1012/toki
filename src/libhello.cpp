#include <iostream>

class User
{
    std::string name;
    public:
        User(char *name):name(name) {}
        User(std::string &name):name(name) {}

        std::string greet() { return "hello, " + name; }
};

void hello(char *name)
{
    User user(name);
    return (void)user.greet();
}

int sum(int a, int b){
    return (a+b);
}
int main()
{
    hello((char *) "world");
    return 0;
}

extern "C"
{
    int cffi_sum(int a, int b)
    {
        return sum(a,b);
    }
    void cffi_hello(char *name)
    {
        return hello(name);
    }
}
