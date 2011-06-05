#lang racket
;;finds if x is divisible by 3 or 5
(define (div-3-5? x)
    (if (or (= (remainder x 3) 0) (= (remainder x 5) 0))
	  true false))

;;generic function to do [start..end]
(define (range start end)
  (if (>= start end) '() (cons start (range (+ 1 start) end))))

(foldl + 0 (filter div-3-5? (range 1 1000)))