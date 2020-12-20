(declare-const b1 Bool)
(declare-const b2 Bool)
(declare-const b3 Bool)
(declare-const b4 Bool)
(declare-const b5 Bool)
(declare-const b6 Bool)

(define-fun Loc1 ((x Int) (y Int)) Int
(ite b1 x y)
)
(define-fun Loc2 ((x Int) (y Int)) Int
(ite b2 x y)
)
(define-fun Loc3 ((x Int) (y Int)) Int
(ite b3 x y)
)
(define-fun Loc4 ((x Int) (y Int)) Int
(ite b4 x y)
)
(define-fun Loc5 ((x Int) (y Int)) Int
(ite b5 x y)
)
(define-fun Loc6 ((x Int) (y Int)) Int
(ite b6 x y)
)

(define-fun lemma ((x Int) (y Int)) Bool
(=> (<= (Loc1 x y) (Loc2 x y))
    (and (<= (Loc3 x y)
             (Loc4 x y))
         (<= (Loc5 x y)
             (Loc6 x y))))
)

(assert (lemma 0 1))
(assert (not (lemma 1 0)))