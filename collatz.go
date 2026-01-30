package main

import (
	// . "fmt"
	"log"
	"math"
	"os/exec"

	"collatz/utils"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
)

var N_SAMPLES = int64(math.Pow(2, 10))

// must be >= 0
var LEFT = float64(1)
var RIGHT = float64(2)

// func f(num int64, den int64) (int64, int64) {
// 	return num, den
// }

func f(num int64, den int64) float64 {
	return float64(utils.U(num)) / float64(utils.U(den))
}

func main() {
	X := make([]float64, N_SAMPLES)
	F := make([]float64, N_SAMPLES)

	sample_density := (RIGHT - LEFT) / float64(N_SAMPLES)
	offset_samples := int64(LEFT / sample_density)

	for i := int64(0); i < N_SAMPLES; i++ {
		num := offset_samples + i
		den := N_SAMPLES
		X[i] = float64(num) / float64(den)
		F[i] = f(num, den)
	}

	p := plot.New()
	p.Title.Text = "f(x)"

	pts := make(plotter.XYs, len(X))
	for i := range X {
		pts[i].X = X[i]
		pts[i].Y = F[i]
	}

	line, _ := plotter.NewLine(pts)
	p.Add(line)

	file := "plot.png"
	if err := p.Save(6*vg.Inch, 4*vg.Inch, file); err != nil {
		log.Fatal(err)
	}
	if err := exec.Command("xdg-open", file).Start(); err != nil {
		log.Fatal(err)
	}
}
