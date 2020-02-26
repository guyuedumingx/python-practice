import java.util.*;
import  java.util.regex.*;

class Opera {
    Pattern pattern = Pattern.compile("^[[0-9\\.]|(]+[\\+\\-\\*/\\^%][[[0-9\\.]|(|)]+[\\+\\-\\*/\\^%]]*[0-9)]$");
    String equation = "";
    String[] save;

    boolean TestLegal(String str) {
        Matcher matcher = pattern.matcher(str);
        if (matcher.find()) {
            equation = matcher.group();
            int left = 0, right = 0, left_number = 0, right_number = 0;
            for (int i = 0; i < equation.length(); i++) {
                if ("(".indexOf(equation.charAt(i)) >= 0) {
                    left += i;
                    left_number++;
                }
                else if (")".indexOf(equation.charAt(i)) >= 0) {
                    right += i;
                    right_number++;
                }
                else if ("+*/%^".indexOf(equation.charAt(i)) >= 0) {
                    if ("0123456789)".indexOf(equation.charAt(i - 1)) < 0) {
                        return false;
                    }
                }
                else if ("-".indexOf(equation.charAt(i)) >= 0) {
                    if ("0123456789()".indexOf(equation.charAt(i-1)) < 0) {
                        return false;
                    }
                }
            }
            if (((left_number == right_number) && (left_number == 0)) || (left_number == right_number) && (left < right)) {
                return true;
            }
            else {
                return false;
            }
        }
        else {
            return false;
        }
    }

    void TransSuffix() {
        String str = equation;
        int n = 0;
        Stack<String> aStack = new Stack<>();
        for (int i = 0; i < str.length(); i++) {
            if (".0123456789".indexOf(str.charAt(i)) >= 0) {
                StringBuilder s = new StringBuilder();
                //实现多位数字的存储
                for (; i < str.length() && ".0123456789".indexOf(str.charAt(i)) >= 0; i++) {
                    s.append(str.charAt(i));
                }
                save[n] = s.toString();
                n++;
                i--;
            }
            else if ("^".indexOf(str.charAt(i)) >= 0) {
                aStack.push(str.substring(i, i + 1));
            }
            else if ("*/%".indexOf(str.charAt(i)) >= 0) {
                // 如果不是空栈
                if (!aStack.isEmpty()) {
                    //如果栈顶元素优先级更高，则先弹出栈顶元素
                    if ("^".indexOf(aStack.peek()) >= 0) {
                        save[n] = aStack.pop();
                        n++;
                    }
                }
                aStack.push(str.substring(i, i + 1));
            }
            else if ("(".indexOf(str.charAt(i)) >= 0) {
                if ("-".indexOf(str.charAt(i + 1)) >= 0) {
                    i += 2;
                    StringBuilder st = new StringBuilder();
                    st.append("-");
                    //实现多位数字的存储
                    for (; i < str.length() && ".0123456789".indexOf(str.charAt(i)) >= 0; i++) {
                        st.append(str.charAt(i));
                    }
                    save[n] = st.toString();
                    n++;
                }
                else {
                    aStack.push(str.substring(i, i + 1));
                }
            }
            else if ("+-".indexOf(str.charAt(i)) >= 0) {
                // 如果不是空栈
                if (!aStack.isEmpty()) {
                    //如果栈顶元素优先级更高，则先弹出栈顶元素
                    if ("*/%^".indexOf(aStack.peek()) >= 0) {
                        save[n] = aStack.pop();
                        n++;
                    }
                }
                aStack.push(str.substring(i, i + 1));
            }
            else if (")".indexOf(str.charAt(i)) >= 0) {
                //如果碰到）则依次取出栈顶元素直到遇到（
                while (true) {
                    String bStack = aStack.pop();
                    if ("(".indexOf(bStack) >= 0) {
                        break;
                    }
                    else {
                        save[n] = bStack;
                        n++;
                    }

                }
            }
        }
        //弹出所有栈内元素，形成后缀表达式并保存在save中
        while (!aStack.isEmpty()) {
            save[n] = aStack.pop();
            n++;
        }

    }

    String GetResult() {
        //实现后缀表达式的计算
        Stack<String> cStack = new Stack<>();
        for (String element : save) {
            if (element == null) {
                break;
            }
            else if ("+-*%/^".indexOf(element) >= 0) {
                double num1, num2, num3 = 0;
                String str1 = cStack.pop();
                String str2 = cStack.pop();
                num1 = Double.parseDouble(str1);
                num2 = Double.parseDouble(str2);
                if ("+".equals(element)) {
                    num3 = num1 + num2;
                }
                else if ("-".equals(element)) {
                    num3 = num2 - num1;
                }
                else if ("*".equals(element)) {
                    num3 = num1 * num2;
                }
                else if ("/".equals(element)) {
                    if (num1 != 0) {
                        num3 = num2 / num1;
                    }
                    //除0错误
                    else {
                        return "0不能做除数";
                    }
                }
                else if ("%".equals(element)) {
                    num3 = num2 % num1;
                }
                else if ("^".equals(element)) {
                    num3 = Math.pow(num2, num1);
                }
                String str3 = String.valueOf(num3);
                cStack.push(str3);
            }
            else {
                cStack.push(element);
            }
        }
        String str4 = cStack.pop();
        return str4;
    }
}


class InOut {
    Scanner in = new Scanner(System.in);

    void Welcome() {
        print("Welcome to Calcuclator");
    }

    String InText() {
        System.out.print("Please enter an equation: ");
        return in.nextLine();
    }

    static void print(String str) {
        System.out.println(str);
    }
}

public class Calculator2 {
    public static void main(String[] args) {
        InOut inout = new InOut();
        Opera opera = new Opera();
        inout.Welcome();
        while (true) {
            opera.save = new String[1000];
            String intext = inout.InText();
            if (opera.TestLegal(intext)) {
                opera.TransSuffix();
                InOut.print(opera.GetResult());
            }
            else if ("q".equalsIgnoreCase(intext)) {
                break;
            }
            else {
                InOut.print("Wrong Input");
            }
        }

    }
}
