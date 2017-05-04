#include <stdio.h>
#include <math.h>

double computeRingProb(double radius, double std_dev){
    return -exp((-1 * radius * radius) / (2 * std_dev * std_dev));
}

int main(){
    double bulleye_rad, bull_rad, inner_triple, outer_triple, inner_double, outer_double,
           std_dev;

    scanf("%lf %lf %lf %lf %lf %lf %lf",&bulleye_rad,&bull_rad,&inner_triple,&outer_triple,&inner_double,&outer_double, &std_dev); 

    double bulleye_prob = 50*(computeRingProb(bulleye_rad,std_dev) - computeRingProb(0,std_dev));
    double bull_prob = 25*(computeRingProb(bull_rad,std_dev) - computeRingProb(bulleye_rad,std_dev));
    double inner3_prob = 10.5*(computeRingProb(inner_triple,std_dev) - computeRingProb(bull_rad,std_dev));
    double outer3_prob = 3*10.5*(computeRingProb(outer_triple,std_dev) - computeRingProb(inner_triple,std_dev));
    double inner2_prob = 10.5*(computeRingProb(inner_double,std_dev) - computeRingProb(outer_triple,std_dev));
    double outer2_prob = 2*10.5*(computeRingProb(outer_double, std_dev) - computeRingProb(inner_double,std_dev));

    printf("%lf",bulleye_prob + bull_prob + inner3_prob + outer3_prob + inner2_prob + outer2_prob);

}
