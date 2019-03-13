#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

double evaluation(char *,size_t);
char * postfix_conversion(char *,size_t);
void pop_element(char *, char *);
void push_element(char *, char);
int has_higher_precedence(char, char);
int is_oporfun(char);
int get_value(char);
int is_right_associative(char);
int whatary(char x);
double binaryeval(char, double, double);
void doublepusher(double *, double, int);
double doublepoper(double *, int);
double unaryeval(char, double);

int main()
{
    char formula[100];
    char *postfix;
    size_t lenformula, lenpostfix;
    double result;

    printf("Please enter the mathematical expression (up to 200 characters)\n");
    fgets(formula, 200, stdin);

    lenformula = strlen(formula);
    formula[lenformula - 1] = 0;
    postfix = postfix_conversion(formula, lenformula);
    lenpostfix = strlen(postfix);
    result = evaluation(postfix, lenpostfix);
    
    printf("Result: %.2lf\n", result);
    return 0;
}

double evaluation(char arr[], size_t len)
{
    // This function evaluates the expression
    int i, indexnumbers = 0;
    double numbers[200] = {0}, num1, num2;
    for (i = 0; i <= len - 1; ++i) {
        if(((arr[i] >= '0' && arr[i] <= '9') && (arr[i - 1] >= '0' && arr[i - 1] <= '9')) || arr[i] == '.' || arr[i - 1] == '.')
            continue;
        else if(is_oporfun(arr[i]))
        {
            if(whatary(arr[i]))
            {
                num2 = doublepoper(numbers,indexnumbers);
                indexnumbers--;
                num1 = doublepoper(numbers,indexnumbers);
                indexnumbers--;
                doublepusher(numbers, binaryeval(arr[i], num1, num2), indexnumbers);
                indexnumbers++;
            }
            else
            {
                num1 = doublepoper(numbers,indexnumbers);
                indexnumbers--;
                doublepusher(numbers, unaryeval(arr[i], num1), indexnumbers);
                indexnumbers++;
            }
        }
        else if(arr[i] == ' ')
            continue;
        else if((arr[i] >= '0' && arr[i] <= '9')) {
            doublepusher(numbers, atof(&arr[i]), indexnumbers);
            indexnumbers++;
        }
    }
    return numbers[0];
}

char * postfix_conversion(char arr[], size_t len)
{
    // This function converts the expression to postfix form
    size_t lenf, lenstack, lenfinal;
    char *final = calloc(200,1);
    char stack[200] = "";
    int i, k, stackindex = 0, j, u = 0, l;
    for (i = 0; i <= len - 1; ++i) {
        if(u != 0 && !((arr[i] >= '0' && arr[i] <= '9') || arr[i] == '.')) {
            final[strlen(final)] = ' ';
            u = 0;
        }
        if(arr[i] == ' ' || arr[i] == 'i' || arr[i] == 'n' || arr[i] == 'q' || arr[i] == 'r' || arr[i] == 't' || arr[i] == 'o')
            continue;
        else if(arr[i] == 's')
        {
            if(arr[i + 1] == 'i')
                arr[i] = 'm';
            else if(arr[i + 1] == 'q')
                arr[i] = 'p';
            else
                continue;
        }
        if(arr[i] == '.')
            push_element(final, arr[i]);
        else if(is_oporfun(arr[i]))
        {
            if(stackindex == 0) {
                stack[stackindex] = arr[i];
                ++stackindex;
            }
            else {
                if(arr[i] == '(') {
                    push_element(stack, arr[i]);
                    ++stackindex;
                }
                else if(arr[i] == ')')
                {
                    for (j = stackindex - 1; j > -1; --j) {
                        if(stack[j] == '(') {
                            stack[j] = 0;
                            --stackindex;
                            break;
                        }
                        else {
                            pop_element(stack, final);
                            --stackindex;
                        }
                    }
                }
                else if(has_higher_precedence(stack[stackindex - 1], arr[i])) {
                    for (l = stackindex; l >= 0; --l) {
                        if(l - 1 < 0)
                        {
                            push_element(stack, arr[i]);
                            ++stackindex;
                            break;
                        }
                        else if (has_higher_precedence(stack[l - 1], arr[i])) {
                            pop_element(stack, final);
                            stack[l - 1] = 0;
                            --stackindex;
                        }
                        else {
                            push_element(stack, arr[i]);
                            ++stackindex;
                            break;
                        }
                    }
                }
                else {
                    push_element(stack, arr[i]);
                    ++stackindex;
                }
            }
        }
        else
        {
            if(arr[i + 1] == '.' || final[strlen(final) - 1] == '.' || ((arr[i] >= '0' && arr[i] <= '9') && (arr[i + 1] >= '0' && arr[i + 1] <= '9')) || ((arr[i] >= '0' && arr[i] <= '9') && (arr[i - 1] >= '0' && arr[i - 1] <= '9')))
            {
                ++u;
                push_element(final,arr[i]);
            }
            else {
                push_element(final, arr[i]);
                lenf = strlen(final);
                final[lenf] = ' ';
            }
        }
    }
    lenstack = strlen(stack);
    lenfinal = strlen(final);
    if(final[lenfinal - 1] >= '0' && final[lenfinal - 1] <= '9')
        final[lenfinal] = ' ';
    lenfinal = strlen(final);
    for (i = lenstack, k = 0; i > 0; ++k,--i) {
        final[lenfinal + k] = stack[i - 1];
    }
    return final;
}

void doublepusher(double x[], double num , int len)
{
    x[len] = num;
}

double doublepoper(double x[], int len)
{
    double temp;
    if(len == 0) {
        temp = x[len];
        x[len] = 0;
    }
    else
    {
        temp = x[len-1];
        x[len-1] = 0;
    }
    return temp;
}

double binaryeval(char op, double x, double y)
{
    double result = .0;
    switch (op)
    {
        case '+':
            result = x + y;
            break;
        case '*':
            result = x * y;
            break;
        case '/':
            result = x / y;
            break;
        case '-':
            result = x - y;
            break;
        case '^':
            result = pow(x,y);
            break;
        default:
            break;
    }
    return result;
}

double unaryeval(char op, double x)
{
    double result =.0;
    switch (op)
    {
        case '~':
            result = -x;
            break;
        case 'l':
            result = log(x);
            break;
        case 'c':
            result = cos(x);
            break;
        case 'm':
            result = sin(x);
            break;
        case 'p':
            result = sqrt(x);
            break;
        default:
            break;
    }
    return result;
}

int is_oporfun(char x)
{
    if(x == '/' || x == '*' || x == '+' || x == '-' || x == '^' || x == '~' || x == 'l' || x == 'c' || x == 'm' || x == '(' || x == ')' || x == 'p')
        return 1;
    else
        return 0;
}

int whatary(char x)
{
    if(x =='/' || x == '*' || x == '+' || x == '-' || x == '^')
        return 1;
    else
        return 0;
}

void pop_element(char st[], char fin[])
{
    size_t lenst = strlen(st), lenfin = strlen(fin);
    if(lenfin == 200)
        return;
    else {
        fin[lenfin] = st[lenst - 1];
        st[lenst - 1] = 0;
    }
}

void push_element(char arr1[], char pushed)
{
    size_t len1 = strlen(arr1);
    if(len1 == 0) {
        arr1[0] = pushed;
        return;
    }
    else if(len1 == 200)
        return;
    else
        arr1[len1] = pushed;
}

int get_value(char x)
{
    int valuex = 0;
    switch (x)
    {
        case 'm':
            valuex = 4;
            break;
        case 'c':
            valuex = 4;
            break;
        case 'p':
            valuex = 4;
            break;
        case 'l':
            valuex = 4;
            break;
        case '~':
            valuex = 4;
            break;
        case '^':
            valuex = 3;
            break;
        case '*':
            valuex = 2;
            break;
        case '/':
            valuex = 2;
            break;
        case '+':
            valuex = 1;
            break;
        case '-':
            valuex = 1;
            break;
        case '(':
            valuex = 0;
        default:
            break;
    }
    return valuex;
}

int has_higher_precedence(char op1,char op2)
{
    int value1 = get_value(op1), value2 = get_value(op2);
    if(value1 == value2)
    {
        if(is_right_associative(op1))
            return 0;
        else
            return 1;
    }
    else
        return value1 > value2 ? 1:0;
}

int is_right_associative(char x)
{
    return x == '^' ? 1:0;
}