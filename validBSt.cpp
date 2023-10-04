#include <bits/stdc++.h>
using namespace std;

bool testBST(vector<int>& input) {
    stack<int> stack;
    int root = -1;

    for (int i : input) {
        if (i < root) {
            return false;
        }

        while (!stack.empty() && stack.top() < i) {
            root = stack.top();
            stack.pop();
        }
        stack.push(i);
    }

    return true;
}

int main() {
    vector<int> input{1,3,4,2};
    bool ans=testBST(input);
    if(ans) cout << "YES";
    else cout << "NO";
}
