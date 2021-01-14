(set-logic ALL)
;; combination of true models and false model
(define-fun hbst ((x!0 Int)) (Set Int)
  (ite (and (= x!0 13808)) (as emptyset (Set Int))
  (ite (and (= x!0 13806)) (insert 13799 (insert 13806 (insert 13810 (insert 13875 (insert 13815 (insert 13819 (as emptyset (Set Int))))))))
  (ite (and (= x!0 13873)) (insert 13798 (insert 13801 (insert 13802 (insert 13803 (insert 13997 (insert 13873 (insert 13874 (insert 13882 (as emptyset (Set Int))))))))))
  (ite (and (= x!0 13813)) (insert 0 (insert 14027 (insert 13804 (insert 13808 (insert 13811 (insert 13876 (insert 13813 (insert 13815 (insert 13821 (as emptyset (Set Int)))))))))))
  (ite (and (= x!0 13800)) (insert 13808 (insert 13817 (insert 13818 (insert 13800 (as emptyset (Set Int))))))
  (ite (and (= x!0 13815)) (insert 13799 (insert 13806 (insert 13810 (insert 13875 (insert 13815 (insert 13819 (as emptyset (Set Int))))))))
  (ite (and (= x!0 13875)) (insert 0 (insert 13997 (insert 13873 (insert 13874 (insert 13875 (insert 13876 (insert 13881 (insert 13882 (insert 14027 (insert 13798 (insert 13801 (insert 13802 (insert 13803 (insert 13804 (insert 13805 (insert 13808 (insert 13811 (insert 13812 (insert 13813 (insert 13815 (insert 13816 (insert 13818 (insert 13821 (as emptyset (Set Int)))))))))))))))))))))))))
  (ite (and (= x!0 13816)) (insert 13816 (insert 13818 (insert 13812 (insert 13805 (as emptyset (Set Int))))))
  (ite (and (= x!0 13818)) (insert 13808 (insert 13817 (insert 13818 (insert 13800 (as emptyset (Set Int))))))
  (ite (and (= x!0 13881)) (insert 13798 (insert 13801 (insert 13802 (insert 13803 (insert 13997 (insert 13805 (insert 13873 (insert 13874 (insert 13812 (insert 13882 (insert 13816 (insert 13881 (insert 13818 (as emptyset (Set Int)))))))))))))))
  (ite (and (= x!0 13804)) (insert 0 (insert 14027 (insert 13804 (insert 13808 (insert 13811 (insert 13876 (insert 13815 (insert 13821 (as emptyset (Set Int))))))))))
  (as emptyset (Set Int))))))))))))))

(define-fun rght ((x!0 Int)) Int
  (ite (= x!0 13808) 13808
  (ite (= x!0 13806) 13936
  (ite (= x!0 13873) 13905
  (ite (= x!0 13813) 13808
  (ite (= x!0 13800) 13924
  (ite (= x!0 13815) 13806
  (ite (= x!0 13875) 13813
  (ite (= x!0 13816) 13946
  (ite (= x!0 13818) 13808
  (ite (= x!0 13881) 13873
  (ite (= x!0 13804) 13914
    13808))))))))))))
(define-fun minr ((x!0 Int)) Int
  (ite (= x!0 13808) 100
  (ite (= x!0 13806) (- 1)
  (ite (= x!0 13873) 12
  (ite (= x!0 13813) 70
  (ite (= x!0 13800) 66
  (ite (= x!0 13815) (- 2)
  (ite (= x!0 13875) 1
  (ite (= x!0 13816) 1
  (ite (= x!0 13818) 65
  (ite (= x!0 13881) 1
  (ite (= x!0 13804) 70
    1))))))))))))
(define-fun lft ((x!0 Int)) Int
  (ite (= x!0 13808) 13808
  (ite (= x!0 13806) 13934
  (ite (= x!0 13873) 13906
  (ite (= x!0 13813) 13804
  (ite (= x!0 13800) 13925
  (ite (= x!0 13815) 13808
  (ite (= x!0 13875) 13881
  (ite (= x!0 13816) 13947
  (ite (= x!0 13818) 13800
  (ite (= x!0 13881) 13816
  (ite (= x!0 13804) 13915
    13808))))))))))))
(define-fun key ((x!0 Int)) Int
  (ite (= x!0 13808) 101
  (ite (= x!0 13806) (- 1)
  (ite (= x!0 13873) 68
  (ite (= x!0 13813) 71
  (ite (= x!0 13800) 67
  (ite (= x!0 13815) (- 2)
  (ite (= x!0 13875) 69
  (ite (= x!0 13816) 1
  (ite (= x!0 13818) 65
  (ite (= x!0 13881) 12
  (ite (= x!0 13804) 70
    101))))))))))))
(define-fun maxr ((x!0 Int)) Int
  (ite (= x!0 13808) (- 1)
  (ite (= x!0 13806) 1
  (ite (= x!0 13873) 68
  (ite (= x!0 13813) 71
  (ite (= x!0 13800) 67
  (ite (= x!0 13815) 1
  (ite (= x!0 13875) 71
  (ite (= x!0 13816) 11
  (ite (= x!0 13818) 67
  (ite (= x!0 13881) 68
  (ite (= x!0 13804) 70
    1))))))))))))
(define-fun bst ((x!0 Int)) Bool
  (ite (= x!0 13808) true
  (ite (= x!0 13806) false
  (ite (= x!0 13873) true
  (ite (= x!0 13813) true
  (ite (= x!0 13800) false
  (ite (= x!0 13815) false
  (ite (= x!0 13875) true
  (ite (= x!0 13816) true
  (ite (= x!0 13818) false
  (ite (= x!0 13881) true
  (ite (= x!0 13804) true
    true))))))))))))

;; lemma to synthesize
;; TODO: must be generated from problem parameters

;Declaring boolean variables to encode grammar
(declare-const lemma_b0 Bool)
(declare-const lemma_b1 Bool)
(declare-const lemma_b2 Bool)
(declare-const lemma_b3 Bool)
(declare-const lemma_b4 Bool)
(declare-const lemma_b5 Bool)
(declare-const lemma_b6 Bool)
(declare-const lemma_b7 Bool)
(declare-const lemma_b8 Bool)
(declare-const lemma_b9 Bool)
(declare-const lemma_b10 Bool)
(declare-const lemma_b11 Bool)
(declare-const lemma_b12 Bool)
(declare-const lemma_b13 Bool)
(declare-const lemma_b14 Bool)
(declare-const lemma_b15 Bool)
(declare-const lemma_b16 Bool)
(declare-const lemma_b17 Bool)
(declare-const lemma_b18 Bool)
(declare-const lemma_b19 Bool)
(declare-const lemma_b20 Bool)
(declare-const lemma_b21 Bool)
(declare-const lemma_b22 Bool)
(declare-const lemma_b23 Bool)
(declare-const lemma_b24 Bool)
(declare-const lemma_b25 Bool)
(declare-const lemma_b26 Bool)
(declare-const lemma_b27 Bool)
(declare-const lemma_b28 Bool)
(declare-const lemma_b29 Bool)
(declare-const lemma_b30 Bool)
(declare-const lemma_b31 Bool)
(declare-const lemma_b32 Bool)
(declare-const lemma_b33 Bool)
(declare-const lemma_b34 Bool)
(declare-const lemma_b35 Bool)
(declare-const lemma_b36 Bool)
(declare-const lemma_b37 Bool)
(declare-const lemma_b38 Bool)
(declare-const lemma_b39 Bool)

;Declaring functions corresponding to nonterminals
;Functions corresponding to Loc
(define-fun lemma_Loc_0 ((x Int) (y Int)) Int
(ite lemma_b2 
 x 
 y)
)
(define-fun lemma_Loc_2 ((x Int) (y Int)) Int
(ite lemma_b5 
 x 
 y)
)
(define-fun lemma_Loc_1 ((x Int) (y Int)) Int
(ite lemma_b6 
 x 
 y)
)
(define-fun lemma_Loc_5 ((x Int) (y Int)) Int
(ite lemma_b11 
 x 
 y)
)
(define-fun lemma_Loc_6 ((x Int) (y Int)) Int
(ite lemma_b12 
 x 
 y)
)
(define-fun lemma_Loc_8 ((x Int) (y Int)) Int
(ite lemma_b13 
 x 
 y)
)
(define-fun lemma_Loc_4 ((x Int) (y Int)) Int
(ite lemma_b14 
 x 
 y)
)
(define-fun lemma_Loc_12 ((x Int) (y Int)) Int
(ite lemma_b17 
 x 
 y)
)
(define-fun lemma_Loc_10 ((x Int) (y Int)) Int
(ite lemma_b22 
 x 
 y)
)
(define-fun lemma_Loc_9 ((x Int) (y Int)) Int
(ite lemma_b23 
 x 
 y)
)
(define-fun lemma_Loc_7 ((x Int) (y Int)) Int
(ite lemma_b24 
 x 
 y)
)
(define-fun lemma_Loc_17 ((x Int) (y Int)) Int
(ite lemma_b25 
 x 
 y)
)
(define-fun lemma_Loc_19 ((x Int) (y Int)) Int
(ite lemma_b26 
 x 
 y)
)
(define-fun lemma_Loc_14 ((x Int) (y Int)) Int
(ite lemma_b29 
 x 
 y)
)
(define-fun lemma_Loc_23 ((x Int) (y Int)) Int
(ite lemma_b30 
 x 
 y)
)
(define-fun lemma_Loc_3 ((x Int) (y Int)) Int
(ite lemma_b31 
 x 
 y)
)
(define-fun lemma_Loc_15 ((x Int) (y Int)) Int
(ite lemma_b32 
 x 
 y)
)
(define-fun lemma_Loc_18 ((x Int) (y Int)) Int
(ite lemma_b33 
 x 
 y)
)
(define-fun lemma_Loc_13 ((x Int) (y Int)) Int
(ite lemma_b34 
 x 
 y)
)
(define-fun lemma_Loc_20 ((x Int) (y Int)) Int
(ite lemma_b35 
 x 
 y)
)
(define-fun lemma_Loc_11 ((x Int) (y Int)) Int
(ite lemma_b36 
 x 
 y)
)
(define-fun lemma_Loc_21 ((x Int) (y Int)) Int
(ite lemma_b37 
 x 
 y)
)
(define-fun lemma_Loc_16 ((x Int) (y Int)) Int
(ite lemma_b38 
 x 
 y)
)
(define-fun lemma_Loc_22 ((x Int) (y Int)) Int
(ite lemma_b39 
 x 
 y)
)
;Functions corresponding to G
(define-fun lemma_G_0 ((x Int) (y Int)) (Set Int)
(hbst (lemma_Loc_4 x y))
)
(define-fun lemma_G_1 ((x Int) (y Int)) (Set Int)
(hbst (lemma_Loc_10 x y))
)
(define-fun lemma_G_2 ((x Int) (y Int)) (Set Int)
(hbst (lemma_Loc_20 x y))
)
;Functions corresponding to H
(define-fun lemma_H_1 ((x Int) (y Int)) Int
(ite lemma_b3 
 (key (lemma_Loc_1 x y)) 
 (ite lemma_b4 
 (minr (lemma_Loc_2 x y)) 
 (maxr (lemma_Loc_3 x y))))
)
(define-fun lemma_H_2 ((x Int) (y Int)) Int
(ite lemma_b8 
 (key (lemma_Loc_6 x y)) 
 (ite lemma_b9 
 (minr (lemma_Loc_7 x y)) 
 (maxr (lemma_Loc_8 x y))))
)
(define-fun lemma_H_4 ((x Int) (y Int)) Int
(ite lemma_b15 
 (key (lemma_Loc_11 x y)) 
 (ite lemma_b16 
 (minr (lemma_Loc_12 x y)) 
 (maxr (lemma_Loc_13 x y))))
)
(define-fun lemma_H_3 ((x Int) (y Int)) Int
(ite lemma_b18 
 (key (lemma_Loc_14 x y)) 
 (ite lemma_b19 
 (minr (lemma_Loc_15 x y)) 
 (maxr (lemma_Loc_16 x y))))
)
(define-fun lemma_H_0 ((x Int) (y Int)) Int
(ite lemma_b20 
 (key (lemma_Loc_17 x y)) 
 (ite lemma_b21 
 (minr (lemma_Loc_18 x y)) 
 (maxr (lemma_Loc_19 x y))))
)
(define-fun lemma_H_5 ((x Int) (y Int)) Int
(ite lemma_b27 
 (key (lemma_Loc_21 x y)) 
 (ite lemma_b28 
 (minr (lemma_Loc_22 x y)) 
 (maxr (lemma_Loc_23 x y))))
)
;Functions corresponding to B1
(define-fun lemma_B1_0 ((x Int) (y Int)) Bool
(ite lemma_b1 
 (<= (lemma_H_0 x y) (lemma_H_0 x y)) 
 (member (lemma_Loc_0 x y) (lemma_G_0 x y)))
)
(define-fun lemma_B1_2 ((x Int) (y Int)) Bool
(ite lemma_b7 
 (<= (lemma_H_2 x y) (lemma_H_2 x y)) 
 (member (lemma_Loc_5 x y) (lemma_G_1 x y)))
)
(define-fun lemma_B1_1 ((x Int) (y Int)) Bool
(ite lemma_b10 
 (<= (lemma_H_4 x y) (lemma_H_4 x y)) 
 (member (lemma_Loc_9 x y) (lemma_G_2 x y)))
)
;Functions corresponding to Start
(define-fun lemma_Start_0 ((x Int) (y Int)) Bool
(ite lemma_b0 
 (lemma_B1_0 x y) 
 (=> (lemma_B1_1 x y) (lemma_B1_1 x y)))
)

;Function to be synthesised
(define-fun lemma ((x Int) (y Int)) Bool
(lemma_Start_0 x y)
)


;Declaring boolean variables to encode grammar


;Declaring functions corresponding to nonterminals
;Functions corresponding to Start
(define-fun rswitch_Start_0 () Int
0
)

;Function to be synthesised
(define-fun rswitch () Int
rswitch_Start_0
)

;; pfp constraints from counterexample models


;; constraints from false model
(assert (or (and (=> (= rswitch 0) (not (=> (bst 13800) (lemma 13800 13800 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13800) (lemma 13800 13804 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13800) (lemma 13800 13806 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13800) (lemma 13800 13808 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13800) (lemma 13800 13873 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13800) (lemma 13800 13875 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13800) (lemma 13800 13813 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13800) (lemma 13800 13815 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13800) (lemma 13800 13816 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13800) (lemma 13800 13881 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13800) (lemma 13800 13818 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13804) (lemma 13804 13800 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13804) (lemma 13804 13804 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13804) (lemma 13804 13806 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13804) (lemma 13804 13808 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13804) (lemma 13804 13873 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13804) (lemma 13804 13875 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13804) (lemma 13804 13813 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13804) (lemma 13804 13815 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13804) (lemma 13804 13816 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13804) (lemma 13804 13881 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13804) (lemma 13804 13818 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13806) (lemma 13806 13800 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13806) (lemma 13806 13804 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13806) (lemma 13806 13806 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13806) (lemma 13806 13808 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13806) (lemma 13806 13873 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13806) (lemma 13806 13875 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13806) (lemma 13806 13813 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13806) (lemma 13806 13815 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13806) (lemma 13806 13816 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13806) (lemma 13806 13881 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13806) (lemma 13806 13818 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13808) (lemma 13808 13800 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13808) (lemma 13808 13804 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13808) (lemma 13808 13806 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13808) (lemma 13808 13808 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13808) (lemma 13808 13873 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13808) (lemma 13808 13875 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13808) (lemma 13808 13813 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13808) (lemma 13808 13815 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13808) (lemma 13808 13816 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13808) (lemma 13808 13881 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13808) (lemma 13808 13818 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13873) (lemma 13873 13800 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13873) (lemma 13873 13804 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13873) (lemma 13873 13806 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13873) (lemma 13873 13808 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13873) (lemma 13873 13873 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13873) (lemma 13873 13875 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13873) (lemma 13873 13813 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13873) (lemma 13873 13815 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13873) (lemma 13873 13816 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13873) (lemma 13873 13881 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13873) (lemma 13873 13818 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13875) (lemma 13875 13800 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13875) (lemma 13875 13804 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13875) (lemma 13875 13806 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13875) (lemma 13875 13808 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13875) (lemma 13875 13873 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13875) (lemma 13875 13875 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13875) (lemma 13875 13813 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13875) (lemma 13875 13815 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13875) (lemma 13875 13816 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13875) (lemma 13875 13881 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13875) (lemma 13875 13818 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13813) (lemma 13813 13800 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13813) (lemma 13813 13804 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13813) (lemma 13813 13806 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13813) (lemma 13813 13808 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13813) (lemma 13813 13873 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13813) (lemma 13813 13875 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13813) (lemma 13813 13813 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13813) (lemma 13813 13815 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13813) (lemma 13813 13816 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13813) (lemma 13813 13881 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13813) (lemma 13813 13818 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13815) (lemma 13815 13800 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13815) (lemma 13815 13804 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13815) (lemma 13815 13806 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13815) (lemma 13815 13808 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13815) (lemma 13815 13873 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13815) (lemma 13815 13875 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13815) (lemma 13815 13813 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13815) (lemma 13815 13815 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13815) (lemma 13815 13816 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13815) (lemma 13815 13881 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13815) (lemma 13815 13818 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13816) (lemma 13816 13800 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13816) (lemma 13816 13804 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13816) (lemma 13816 13806 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13816) (lemma 13816 13808 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13816) (lemma 13816 13873 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13816) (lemma 13816 13875 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13816) (lemma 13816 13813 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13816) (lemma 13816 13815 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13816) (lemma 13816 13816 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13816) (lemma 13816 13881 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13816) (lemma 13816 13818 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13881) (lemma 13881 13800 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13881) (lemma 13881 13804 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13881) (lemma 13881 13806 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13881) (lemma 13881 13808 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13881) (lemma 13881 13873 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13881) (lemma 13881 13875 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13881) (lemma 13881 13813 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13881) (lemma 13881 13815 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13881) (lemma 13881 13816 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13881) (lemma 13881 13881 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13881) (lemma 13881 13818 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13818) (lemma 13818 13800 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13818) (lemma 13818 13804 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13818) (lemma 13818 13806 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13818) (lemma 13818 13808 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13818) (lemma 13818 13873 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13818) (lemma 13818 13875 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13818) (lemma 13818 13813 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13818) (lemma 13818 13815 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13818) (lemma 13818 13816 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13818) (lemma 13818 13881 ))))
)
(and (=> (= rswitch 0) (not (=> (bst 13818) (lemma 13818 13818 ))))
)
))

;; constraints from true models

(check-sat)(get-model)