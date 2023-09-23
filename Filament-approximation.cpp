#include<iostream>
#include<math.h> //for exponents pow(zahl, exp)

int length(double r1,double r2,double b,double d_f, double density){
    const double pi = 3.14159265358979323846;
    double n = (r2-r1)/d_f ;// layers of filament
    double rows = (b/d_f)-1 ;//-1 because the upper layer is mostly never full
    n = floor(n); //rounds the number down
    rows = floor(rows);

    if (n > 100){
        std::cout <<"number "<< n << " of layers is to big"; //prevents unrealistic too long calculations
    }
    else {
        double L = 0; // Length of filament
        double A = pi*pow((d_f/2),2);

        for (int k = 1; k<=n; k++){ 
            double l = 2*pi*(r1+d_f*k-d_f/2)*rows; //calculates the circumference of every layer
            L += l ;
            
        }
    
        double V = 0.9*pow(10,-3)*L; //actual length in meters; multiplyed by .9 to concider the error
        double Vol = A*V; //Volume = crossare * length
        double m = Vol*density;

        bool warning = true; //turn to false if warnings are unwanted

        if(warning == true){
            //this warns you when you may have entered wrong values
            if (r1 >= r2){
                std::cout << "r2 needs to be greater than r1! " << V << " is not the lenght of your filament!" << '\n';
            }
            if (r1 > b){//for some spools this is normal
                std::cout << "r1 = " << r1 << " is greater than b = " << b << " are you sure you entered the right parameters?" << '\n';
            }
            if (d_f > 3){
                std::cout << "d_f = " << d_f << " is greater than 3 are you sure you entered the right parameters?" << '\n';
            }
            if (0 >= r1 or 0 >= r2 or 0 >= b or 0 >= d_f or 0 >= density){
                std::cout << "You entered a negative number the calculation is wrong!"<< '\n';
            }
        }
        //returns the result
        std::cout << "length: " << V << " [m]" << '\n';
        std::cout << "mass: " << m << " [g]"<< '\n';
        std::cout <<"layers: " << n << '\n';
        std::cout << "density used: " << density << " [g/cm^3]" << '\n';
        
    }
    return 0;
}

//you can add functions with the saved spool measurements, so you only need to insert r2
int Giantarm(double r2,double density){
    length(40,r2,53,1.75,density);
    return 0;
}

int eSun(double r2,double density){
    length(95/2,r2,57,1.75,density);
    return 0;
}

int Prima3d(double r2, double density){
    length(52,r2,45,1.75,density);
    return 0;
}

int functionselect(std::string Funktion){
    double value, density;
    std::cout << "You selected "<< Funktion << '\n';
    std::cout << "r2?" << '\n';
    
    return 0;
}

int main(){
    int funktion;
    std::cout << "Available functions: 1. eSun, 2. Giantarm, 3. Prima3d" << '\n';
    std::cout << "function?" << '\n';
    std::cin >> funktion;

    switch(funktion){
        case 1:
            double value;
            functionselect("eSun");
            eSun(value,1.25);
            break;
        
        case 2:
            double density;
            std::cout << "You selected Giantarm" << '\n';
            std::cout << "r2?" << '\n';
            std::cin >>  value;
            std::cout << "density?" << '\n';
            std::cin >>  density;
            Giantarm(value, density);
            break;

        case 3:
            std::cout << "You selected Prima3d" << '\n';
            std::cout << "r2?" << '\n';
            std::cin >>  value;
            std::cout << "density?" << '\n';
            std::cin >>  density;
            Prima3d(value, density);
            break;
//if non of the presaved functions shold be used write something else and select all the parameters manually
        default:
            double r_1, r_2, B, Density;
            std::cout << "function not found!"<< '\n';     

            std::cout << "insert all parameters:" << '\n';
            std::cout << "r1" << '\n';
            std::cin >>r_1;

            std::cout << "r2" << '\n';
            std::cin >>r_2;

            std::cout << "width" << '\n';
            std::cin >>B;
            //you can make d_f also variable if you have different printers

            std::cout << "desnity" << '\n';
            std::cin >>Density;
            length(r_1, r_2, B, 1.75, Density);


    }

    return 0;
}
