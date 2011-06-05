(define (fibo-driver n a b)
  (if (= n 0) '()
    (cons (+ a b) (fibo-driver (- n 1) (+ a b) a))))
	
(define (fibo n)
  (fibo-driver n 0 1))
  
(foldl + 0 (filter (lambda (x) (and (= 0 (remainder x 2)) (< x 4000000))) (fibo 35)))