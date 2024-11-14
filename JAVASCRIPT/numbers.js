// tipo de dato: number

// entero y decimal
const entero = 42
const decimal = 3.14

console.log(typeof entero, typeof decimal)

// notacion cientifica
const cientifico = 5e3

// infinitos y NaN
const infinitos = Infinity
const noEsUnNumero = NaN

// operaciones aritmeticas
// suma, resta, multiplicacion, division
const suma = 2 + 3
const resta = 5 - 2
const multiplicacion = 2 * 4
const division = 10 / 2

console.log(suma, resta, multiplicacion, division)

// moudulo, explonenciacion
const modulo = 10 % 3 // Sirve para sacar el resto de la division
const exponenciacion = 2 ** 3 // Sirve para elevar a la potencia

console.log(modulo, exponenciacion)

// presicion
const presicion = 0.1 + 0.2

console.log(presicion)
console.log(presicion.toFixed(1)) // Redondea a 1 decimal
console.log(presicion === 0.3) // Compara si es igual a 0.3 a nivel de numero y tipo de dato

// operaciones avanzadas
const raizCuadrada = Math.sqrt(16) // Sirve para calcular la raiz cuadrada de un numero
const valorAbsoluto = Math.abs(-5) // Sirve para calcular el valor absoluto de un numero
const aleatorio = Math.random().toFixed(2) // Sirve para generar un numero aleatorio entre 0 y 1

console.log(raizCuadrada, valorAbsoluto, aleatorio)
