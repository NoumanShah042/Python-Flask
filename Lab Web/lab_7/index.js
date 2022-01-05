function inputEquation(text) {
    document.getElementById("equation").value += text;
}
function calculate() {
    console.log(document.getElementById("equation").value)
    document.getElementById("equation").value = "result"
}
function clearAll() {
    console.log("cleared")
    document.getElementById("equation").value = "";
}
function backspace() {
    console.log("backspace")
    val = document.getElementById("equation").value;
    if (val.length == 0) {
        return;
    }
    val = val.slice(0, val.length - 1)
    document.getElementById("equation").value = val;

}
function getOPerator(val) {
    if (val.includes("+")) {
        return val.indexOf("+")
    }
    else if (val.includes("-")) {
        return val.indexOf("-")
    }
    else if (val.includes("*")) {
        return val.indexOf("*")
    }
    else if (val.includes("/")) {
        return val.indexOf("/")
    }
    else if (val.includes("/")) {
        return val.indexOf("/")
    }
    else {
        return -1;
    }
}

function validateOperands(opr) {
    if (isNaN(opr)) {
        return -1;
    }
    else {
        return parseFloat(opr);
    }
}

function finalcalc(op1, op2, opr) {

    if (opr == '+') {
        document.getElementById("equation").value = op1 + op2
    }
    else if (opr == '-') {
        document.getElementById("equation").value = op1 - op2
    }
    else if (opr == '*') {
        document.getElementById("equation").value = op1 * op2.toFixed(5);
    }
    else if (opr == '/') {
        if (op2 == 0) {
            alert("cannot divide by 0")
            return;
        }
        document.getElementById("equation").value = (op1 / op2).toFixed(5);
    }
}

function calculateResult() {
    val = document.getElementById("equation").value
    if (val.length == 0) {
        alert("Input Expression");
        return;
    }

    let op1, op2, opreator_;   

    opreator_ = getOPerator(val)   //  validating operator
    if (opreator_ == -1) {
        alert("Input valid Expression")
        return;
    }

    //  operator is valid , now we validate operands

    op1 = val.slice(0, opreator_)
    op2 = val.slice(opreator_ + 1, val.length)

    op1 = validateOperands(op1);
    if (validateOperands(op1) == -1) {
        alert("invalid  Expression")
        return;
    }

    op2 = validateOperands(op2);
    if (validateOperands(op2) == -1) {
        alert("invalid Expression")
        return;
    } 
    console.log(op1, op2, val[opreator_])  //  our equation is valid so going to get output 
    finalcalc(op1, op2, val[opreator_]);

}