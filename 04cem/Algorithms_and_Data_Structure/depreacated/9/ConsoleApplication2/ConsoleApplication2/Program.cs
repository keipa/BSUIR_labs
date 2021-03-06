﻿#include <iostream>


using namespace std;

long long how_rise = 0;

int CheckStack(int* stack, int ver_index)
{

    if (ver_index >= 2)
    {
        if (stack[ver_index - 1] < stack[ver_index] && stack[ver_index - 2] < stack[ver_index])
        {
            how_rise += stack[ver_index - 2] - stack[ver_index - 1];
            stack[ver_index - 1] = stack[ver_index];
            ver_index -= 1;
            ver_index = CheckStack(stack, ver_index);
        }
        else if (stack[ver_index - 1] < stack[ver_index] && stack[ver_index - 2] > stack[ver_index])
        {
            how_rise += stack[ver_index] - stack[ver_index - 1];
            stack[ver_index - 1] = stack[ver_index];
            ver_index -= 1;
        }
    }
    else if (ver_index == 1)
    {
        if (stack[ver_index - 1] < stack[ver_index])
        {
            how_rise += stack[ver_index] - stack[ver_index - 1];
            stack[ver_index - 1] = stack[ver_index];
            ver_index -= 1;
        }
    }
    return ver_index;


}
void CollapseStack(int* stack, int ver_index)
{
    int go_down = ver_index - 1;
    while (go_down >= 0)
    {
        how_rise += stack[go_down] - stack[ver_index];
        --go_down;
        --ver_index;
    }
}

int main(void)
{
    int n = 0;
    cin >> n;
    int* nums = new int[n];
    int* stack = new int[n];
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }
    int ver = -1;
    for (int i = 0; i < n; i++)
    {

        ++ver;
        stack[ver] = nums[i];
        if (ver == 0)
        {
            continue;
        }
        else
        {
            if (stack[ver - 1] > stack[ver])
            {
                continue;
            }
            else
            {
                ver = CheckStack(stack, ver);
            }
        }
    }

    CollapseStack(stack, ver);
    cout << how_rise;


    return 0;
}