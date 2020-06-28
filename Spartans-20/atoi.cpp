int Solution::atoi(const string A) {
    stringstream s(A);
    int x{0};
    s>>x;
    return x;
}