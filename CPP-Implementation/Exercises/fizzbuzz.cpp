#include<vector>
#include<string>
using namespace std;

vector<string> fizzbuzz(int n){

    vector<string> result = {};

    for(int num=1; num<=n; num++){
        //number multiples of both 3 and 5 would be multiples of 15 (LCM)
        if (num%15==0){
            result.push_back("FizzBuzz");
        }
        else if (num%5==0){
            result.push_back("Buzz");
        }
        else if (num%3==0){
            result.push_back("Fizz");
        }
        else {
            result.push_back(std::to_string(num));
        }
    }

    return result;

}