package opt

import (
	"collatz/utils"
	"math"
	"math/rand"
	"time"
	. "fmt"
)

const N = 10
const SAMPLES = 10
const COEF_RANGE = N

func randomCoefs(rng *rand.Rand) [N]float64 {
	var coefs [N]float64
	for i := 0; i < N; i++ {
		coefs[i] = -COEF_RANGE + rng.Float64() * 2 * COEF_RANGE
	}
	return coefs
}

func comp(x int, coefs [N]float64) float64 {
	ans := 0.
	for i, coef := range coefs {
		ans += utils.Pin(float64(x), i) * coef
	}
	return ans
}

func fitness(coefs [N]float64) float64 {
	err := 0.
	for i := 1; i <= SAMPLES; i++ {
		err += math.Pow(utils.U(int64(i))-comp(i, coefs), 2.)
	}
	return err
}

func opt() {
	rng := rand.New(rand.NewSource(time.Now().UnixNano()))
	coefs := randomCoefs(rng)
	err := fitness(coefs)
	Println(err)
}
