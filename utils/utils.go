package utils

import (
	// "fmt"
	. "math"
	"log"
)

var B = 2 * Pi / Log(2)

func Pin(t float64, n int) float64 {
	return Sin(float64(n) * float64(Pi) * Log2(t))
}

func Pos(t float64, n int) float64 {
	return Cos(float64(n) * float64(Pi) * Log2(t))
}

func U(n int64) float64 {
	cur := n
	for cur % 2 == 0 {
		cur /= 2
	}
	return float64(cur)
}

func ProductCoefs(F []float64, X []float64, numCoefs int) []float64 {
	if len(F) != len(X) {
		log.Fatal("length of X and F do not match")
	}
	dx := X[1] - X[0]
	coefs := make([]float64, numCoefs)
	for i := 0; i < len(X); i++ {
		x := X[i]
		f := F[i]

		if x == 0 {
			continue
		}

		for k := 0; k < numCoefs; k++ {
			coefs[k] += (f * Cos( - Log(x) * float64(k) * B ) * dx) / (x * Log(2))
		}
	}
	return coefs
}
