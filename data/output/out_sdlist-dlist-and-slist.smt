(set-logic ALL)
;; combination of true models and false model
(define-fun sdlst ((x!0 Int)) Bool
  (ite (= x!0 2) true
  (ite (= x!0 4) true
  (ite (= x!0 1) true
  (ite (= x!0 3) true
  (ite (= x!0 5) true
    true))))))
(define-fun prv ((x!0 Int)) Int
  (ite (= x!0 2) 2
  (ite (= x!0 4) 3
  (ite (= x!0 1) 3
  (ite (= x!0 3) 1
  (ite (= x!0 5) 4
    3))))))
(define-fun key ((x!0 Int)) Int
  (ite (= x!0 2) 0
  (ite (= x!0 4) 0
  (ite (= x!0 1) 0
  (ite (= x!0 3) 0
  (ite (= x!0 5) 0
    0))))))
(define-fun nxt ((x!0 Int)) Int
  (ite (= x!0 2) 2
  (ite (= x!0 4) 5
  (ite (= x!0 1) 3
  (ite (= x!0 3) 4
  (ite (= x!0 5) 3
    3))))))
(define-fun dlst ((x!0 Int)) Bool
  (ite (= x!0 2) true
  (ite (= x!0 4) false
  (ite (= x!0 1) false
  (ite (= x!0 3) false
  (ite (= x!0 5) false
    false))))))
(define-fun slst ((x!0 Int)) Bool
  (ite (= x!0 2) true
  (ite (= x!0 4) false
  (ite (= x!0 1) false
  (ite (= x!0 3) false
  (ite (= x!0 5) false
    false))))))

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
(declare-const lemma_b40 Bool)
(declare-const lemma_b41 Bool)
(declare-const lemma_b42 Bool)
(declare-const lemma_b43 Bool)
(declare-const lemma_b44 Bool)
(declare-const lemma_b45 Bool)
(declare-const lemma_b46 Bool)
(declare-const lemma_b47 Bool)
(declare-const lemma_b48 Bool)
(declare-const lemma_b49 Bool)
(declare-const lemma_b50 Bool)
(declare-const lemma_b51 Bool)
(declare-const lemma_b52 Bool)
(declare-const lemma_b53 Bool)
(declare-const lemma_b54 Bool)
(declare-const lemma_b55 Bool)
(declare-const lemma_b56 Bool)
(declare-const lemma_b57 Bool)
(declare-const lemma_b58 Bool)
(declare-const lemma_b59 Bool)
(declare-const lemma_b60 Bool)
(declare-const lemma_b61 Bool)
(declare-const lemma_b62 Bool)
(declare-const lemma_b63 Bool)
(declare-const lemma_b64 Bool)
(declare-const lemma_b65 Bool)
(declare-const lemma_b66 Bool)
(declare-const lemma_b67 Bool)
(declare-const lemma_b68 Bool)
(declare-const lemma_b69 Bool)
(declare-const lemma_b70 Bool)
(declare-const lemma_b71 Bool)
(declare-const lemma_b72 Bool)
(declare-const lemma_b73 Bool)
(declare-const lemma_b74 Bool)
(declare-const lemma_b75 Bool)
(declare-const lemma_b76 Bool)
(declare-const lemma_b77 Bool)
(declare-const lemma_b78 Bool)
(declare-const lemma_b79 Bool)
(declare-const lemma_b80 Bool)
(declare-const lemma_b81 Bool)
(declare-const lemma_b82 Bool)
(declare-const lemma_b83 Bool)
(declare-const lemma_b84 Bool)
(declare-const lemma_b85 Bool)
(declare-const lemma_b86 Bool)
(declare-const lemma_b87 Bool)
(declare-const lemma_b88 Bool)
(declare-const lemma_b89 Bool)
(declare-const lemma_b90 Bool)
(declare-const lemma_b91 Bool)
(declare-const lemma_b92 Bool)
(declare-const lemma_b93 Bool)
(declare-const lemma_b94 Bool)
(declare-const lemma_b95 Bool)
(declare-const lemma_b96 Bool)
(declare-const lemma_b97 Bool)
(declare-const lemma_b98 Bool)
(declare-const lemma_b99 Bool)
(declare-const lemma_b100 Bool)
(declare-const lemma_b101 Bool)
(declare-const lemma_b102 Bool)
(declare-const lemma_b103 Bool)
(declare-const lemma_b104 Bool)
(declare-const lemma_b105 Bool)
(declare-const lemma_b106 Bool)
(declare-const lemma_b107 Bool)
(declare-const lemma_b108 Bool)
(declare-const lemma_b109 Bool)
(declare-const lemma_b110 Bool)
(declare-const lemma_b111 Bool)
(declare-const lemma_b112 Bool)
(declare-const lemma_b113 Bool)
(declare-const lemma_b114 Bool)
(declare-const lemma_b115 Bool)
(declare-const lemma_b116 Bool)
(declare-const lemma_b117 Bool)
(declare-const lemma_b118 Bool)
(declare-const lemma_b119 Bool)
(declare-const lemma_b120 Bool)
(declare-const lemma_b121 Bool)
(declare-const lemma_b122 Bool)
(declare-const lemma_b123 Bool)
(declare-const lemma_b124 Bool)
(declare-const lemma_b125 Bool)
(declare-const lemma_b126 Bool)
(declare-const lemma_b127 Bool)
(declare-const lemma_b128 Bool)
(declare-const lemma_b129 Bool)
(declare-const lemma_b130 Bool)
(declare-const lemma_b131 Bool)
(declare-const lemma_b132 Bool)
(declare-const lemma_b133 Bool)
(declare-const lemma_b134 Bool)
(declare-const lemma_b135 Bool)
(declare-const lemma_b136 Bool)
(declare-const lemma_b137 Bool)
(declare-const lemma_b138 Bool)
(declare-const lemma_b139 Bool)

;Declaring functions corresponding to nonterminals
;Functions corresponding to I1
(define-fun lemma_I1_0 ((x Int) (nil Int)) Int
(ite lemma_b12 
 x 
 nil)
)
(define-fun lemma_I1_1 ((x Int) (nil Int)) Int
(ite lemma_b19 
 x 
 nil)
)
(define-fun lemma_I1_3 ((x Int) (nil Int)) Int
(ite lemma_b22 
 x 
 nil)
)
(define-fun lemma_I1_7 ((x Int) (nil Int)) Int
(ite lemma_b25 
 x 
 nil)
)
(define-fun lemma_I1_2 ((x Int) (nil Int)) Int
(ite lemma_b28 
 x 
 nil)
)
(define-fun lemma_I1_5 ((x Int) (nil Int)) Int
(ite lemma_b29 
 x 
 nil)
)
(define-fun lemma_I1_8 ((x Int) (nil Int)) Int
(ite lemma_b30 
 x 
 nil)
)
(define-fun lemma_I1_14 ((x Int) (nil Int)) Int
(ite lemma_b37 
 x 
 nil)
)
(define-fun lemma_I1_17 ((x Int) (nil Int)) Int
(ite lemma_b42 
 x 
 nil)
)
(define-fun lemma_I1_4 ((x Int) (nil Int)) Int
(ite lemma_b43 
 x 
 nil)
)
(define-fun lemma_I1_9 ((x Int) (nil Int)) Int
(ite lemma_b44 
 x 
 nil)
)
(define-fun lemma_I1_10 ((x Int) (nil Int)) Int
(ite lemma_b49 
 x 
 nil)
)
(define-fun lemma_I1_11 ((x Int) (nil Int)) Int
(ite lemma_b52 
 x 
 nil)
)
(define-fun lemma_I1_29 ((x Int) (nil Int)) Int
(ite lemma_b53 
 x 
 nil)
)
(define-fun lemma_I1_6 ((x Int) (nil Int)) Int
(ite lemma_b58 
 x 
 nil)
)
(define-fun lemma_I1_12 ((x Int) (nil Int)) Int
(ite lemma_b59 
 x 
 nil)
)
(define-fun lemma_I1_19 ((x Int) (nil Int)) Int
(ite lemma_b68 
 x 
 nil)
)
(define-fun lemma_I1_24 ((x Int) (nil Int)) Int
(ite lemma_b69 
 x 
 nil)
)
(define-fun lemma_I1_33 ((x Int) (nil Int)) Int
(ite lemma_b70 
 x 
 nil)
)
(define-fun lemma_I1_46 ((x Int) (nil Int)) Int
(ite lemma_b71 
 x 
 nil)
)
(define-fun lemma_I1_45 ((x Int) (nil Int)) Int
(ite lemma_b72 
 x 
 nil)
)
(define-fun lemma_I1_16 ((x Int) (nil Int)) Int
(ite lemma_b73 
 x 
 nil)
)
(define-fun lemma_I1_13 ((x Int) (nil Int)) Int
(ite lemma_b74 
 x 
 nil)
)
(define-fun lemma_I1_31 ((x Int) (nil Int)) Int
(ite lemma_b75 
 x 
 nil)
)
(define-fun lemma_I1_39 ((x Int) (nil Int)) Int
(ite lemma_b76 
 x 
 nil)
)
(define-fun lemma_I1_23 ((x Int) (nil Int)) Int
(ite lemma_b77 
 x 
 nil)
)
(define-fun lemma_I1_41 ((x Int) (nil Int)) Int
(ite lemma_b78 
 x 
 nil)
)
(define-fun lemma_I1_35 ((x Int) (nil Int)) Int
(ite lemma_b83 
 x 
 nil)
)
(define-fun lemma_I1_32 ((x Int) (nil Int)) Int
(ite lemma_b86 
 x 
 nil)
)
(define-fun lemma_I1_42 ((x Int) (nil Int)) Int
(ite lemma_b87 
 x 
 nil)
)
(define-fun lemma_I1_28 ((x Int) (nil Int)) Int
(ite lemma_b88 
 x 
 nil)
)
(define-fun lemma_I1_34 ((x Int) (nil Int)) Int
(ite lemma_b89 
 x 
 nil)
)
(define-fun lemma_I1_15 ((x Int) (nil Int)) Int
(ite lemma_b90 
 x 
 nil)
)
(define-fun lemma_I1_21 ((x Int) (nil Int)) Int
(ite lemma_b93 
 x 
 nil)
)
(define-fun lemma_I1_30 ((x Int) (nil Int)) Int
(ite lemma_b94 
 x 
 nil)
)
(define-fun lemma_I1_48 ((x Int) (nil Int)) Int
(ite lemma_b95 
 x 
 nil)
)
(define-fun lemma_I1_18 ((x Int) (nil Int)) Int
(ite lemma_b96 
 x 
 nil)
)
(define-fun lemma_I1_25 ((x Int) (nil Int)) Int
(ite lemma_b97 
 x 
 nil)
)
(define-fun lemma_I1_36 ((x Int) (nil Int)) Int
(ite lemma_b100 
 x 
 nil)
)
(define-fun lemma_I1_58 ((x Int) (nil Int)) Int
(ite lemma_b101 
 x 
 nil)
)
(define-fun lemma_I1_20 ((x Int) (nil Int)) Int
(ite lemma_b104 
 x 
 nil)
)
(define-fun lemma_I1_44 ((x Int) (nil Int)) Int
(ite lemma_b105 
 x 
 nil)
)
(define-fun lemma_I1_27 ((x Int) (nil Int)) Int
(ite lemma_b106 
 x 
 nil)
)
(define-fun lemma_I1_60 ((x Int) (nil Int)) Int
(ite lemma_b107 
 x 
 nil)
)
(define-fun lemma_I1_50 ((x Int) (nil Int)) Int
(ite lemma_b108 
 x 
 nil)
)
(define-fun lemma_I1_26 ((x Int) (nil Int)) Int
(ite lemma_b109 
 x 
 nil)
)
(define-fun lemma_I1_47 ((x Int) (nil Int)) Int
(ite lemma_b110 
 x 
 nil)
)
(define-fun lemma_I1_55 ((x Int) (nil Int)) Int
(ite lemma_b111 
 x 
 nil)
)
(define-fun lemma_I1_49 ((x Int) (nil Int)) Int
(ite lemma_b114 
 x 
 nil)
)
(define-fun lemma_I1_71 ((x Int) (nil Int)) Int
(ite lemma_b117 
 x 
 nil)
)
(define-fun lemma_I1_40 ((x Int) (nil Int)) Int
(ite lemma_b118 
 x 
 nil)
)
(define-fun lemma_I1_51 ((x Int) (nil Int)) Int
(ite lemma_b119 
 x 
 nil)
)
(define-fun lemma_I1_22 ((x Int) (nil Int)) Int
(ite lemma_b120 
 x 
 nil)
)
(define-fun lemma_I1_37 ((x Int) (nil Int)) Int
(ite lemma_b121 
 x 
 nil)
)
(define-fun lemma_I1_52 ((x Int) (nil Int)) Int
(ite lemma_b122 
 x 
 nil)
)
(define-fun lemma_I1_53 ((x Int) (nil Int)) Int
(ite lemma_b123 
 x 
 nil)
)
(define-fun lemma_I1_43 ((x Int) (nil Int)) Int
(ite lemma_b124 
 x 
 nil)
)
(define-fun lemma_I1_56 ((x Int) (nil Int)) Int
(ite lemma_b125 
 x 
 nil)
)
(define-fun lemma_I1_63 ((x Int) (nil Int)) Int
(ite lemma_b126 
 x 
 nil)
)
(define-fun lemma_I1_38 ((x Int) (nil Int)) Int
(ite lemma_b127 
 x 
 nil)
)
(define-fun lemma_I1_67 ((x Int) (nil Int)) Int
(ite lemma_b128 
 x 
 nil)
)
(define-fun lemma_I1_57 ((x Int) (nil Int)) Int
(ite lemma_b129 
 x 
 nil)
)
(define-fun lemma_I1_66 ((x Int) (nil Int)) Int
(ite lemma_b130 
 x 
 nil)
)
(define-fun lemma_I1_65 ((x Int) (nil Int)) Int
(ite lemma_b131 
 x 
 nil)
)
(define-fun lemma_I1_59 ((x Int) (nil Int)) Int
(ite lemma_b132 
 x 
 nil)
)
(define-fun lemma_I1_61 ((x Int) (nil Int)) Int
(ite lemma_b133 
 x 
 nil)
)
(define-fun lemma_I1_69 ((x Int) (nil Int)) Int
(ite lemma_b134 
 x 
 nil)
)
(define-fun lemma_I1_62 ((x Int) (nil Int)) Int
(ite lemma_b135 
 x 
 nil)
)
(define-fun lemma_I1_54 ((x Int) (nil Int)) Int
(ite lemma_b136 
 x 
 nil)
)
(define-fun lemma_I1_64 ((x Int) (nil Int)) Int
(ite lemma_b137 
 x 
 nil)
)
(define-fun lemma_I1_68 ((x Int) (nil Int)) Int
(ite lemma_b138 
 x 
 nil)
)
(define-fun lemma_I1_70 ((x Int) (nil Int)) Int
(ite lemma_b139 
 x 
 nil)
)
;Functions corresponding to I
(define-fun lemma_I_2 ((x Int) (nil Int)) Int
(ite lemma_b10 
 (lemma_I1_0 x nil) 
 (ite lemma_b11 
 (nxt (lemma_I1_1 x nil)) 
 (prv (lemma_I1_2 x nil))))
)
(define-fun lemma_I_6 ((x Int) (nil Int)) Int
(ite lemma_b13 
 (lemma_I1_3 x nil) 
 (ite lemma_b14 
 (nxt (lemma_I1_4 x nil)) 
 (prv (lemma_I1_5 x nil))))
)
(define-fun lemma_I_0 ((x Int) (nil Int)) Int
(ite lemma_b15 
 (lemma_I1_6 x nil) 
 (ite lemma_b16 
 (nxt (lemma_I1_7 x nil)) 
 (prv (lemma_I1_8 x nil))))
)
(define-fun lemma_I_7 ((x Int) (nil Int)) Int
(ite lemma_b17 
 (lemma_I1_9 x nil) 
 (ite lemma_b18 
 (nxt (lemma_I1_10 x nil)) 
 (prv (lemma_I1_11 x nil))))
)
(define-fun lemma_I_8 ((x Int) (nil Int)) Int
(ite lemma_b20 
 (lemma_I1_12 x nil) 
 (ite lemma_b21 
 (nxt (lemma_I1_13 x nil)) 
 (prv (lemma_I1_14 x nil))))
)
(define-fun lemma_I_12 ((x Int) (nil Int)) Int
(ite lemma_b33 
 (lemma_I1_15 x nil) 
 (ite lemma_b34 
 (nxt (lemma_I1_16 x nil)) 
 (prv (lemma_I1_17 x nil))))
)
(define-fun lemma_I_4 ((x Int) (nil Int)) Int
(ite lemma_b35 
 (lemma_I1_18 x nil) 
 (ite lemma_b36 
 (nxt (lemma_I1_19 x nil)) 
 (prv (lemma_I1_20 x nil))))
)
(define-fun lemma_I_10 ((x Int) (nil Int)) Int
(ite lemma_b45 
 (lemma_I1_21 x nil) 
 (ite lemma_b46 
 (nxt (lemma_I1_22 x nil)) 
 (prv (lemma_I1_23 x nil))))
)
(define-fun lemma_I_16 ((x Int) (nil Int)) Int
(ite lemma_b47 
 (lemma_I1_24 x nil) 
 (ite lemma_b48 
 (nxt (lemma_I1_25 x nil)) 
 (prv (lemma_I1_26 x nil))))
)
(define-fun lemma_I_17 ((x Int) (nil Int)) Int
(ite lemma_b50 
 (lemma_I1_27 x nil) 
 (ite lemma_b51 
 (nxt (lemma_I1_28 x nil)) 
 (prv (lemma_I1_29 x nil))))
)
(define-fun lemma_I_3 ((x Int) (nil Int)) Int
(ite lemma_b54 
 (lemma_I1_30 x nil) 
 (ite lemma_b55 
 (nxt (lemma_I1_31 x nil)) 
 (prv (lemma_I1_32 x nil))))
)
(define-fun lemma_I_19 ((x Int) (nil Int)) Int
(ite lemma_b56 
 (lemma_I1_33 x nil) 
 (ite lemma_b57 
 (nxt (lemma_I1_34 x nil)) 
 (prv (lemma_I1_35 x nil))))
)
(define-fun lemma_I_5 ((x Int) (nil Int)) Int
(ite lemma_b60 
 (lemma_I1_36 x nil) 
 (ite lemma_b61 
 (nxt (lemma_I1_37 x nil)) 
 (prv (lemma_I1_38 x nil))))
)
(define-fun lemma_I_1 ((x Int) (nil Int)) Int
(ite lemma_b62 
 (lemma_I1_39 x nil) 
 (ite lemma_b63 
 (nxt (lemma_I1_40 x nil)) 
 (prv (lemma_I1_41 x nil))))
)
(define-fun lemma_I_9 ((x Int) (nil Int)) Int
(ite lemma_b64 
 (lemma_I1_42 x nil) 
 (ite lemma_b65 
 (nxt (lemma_I1_43 x nil)) 
 (prv (lemma_I1_44 x nil))))
)
(define-fun lemma_I_11 ((x Int) (nil Int)) Int
(ite lemma_b66 
 (lemma_I1_45 x nil) 
 (ite lemma_b67 
 (nxt (lemma_I1_46 x nil)) 
 (prv (lemma_I1_47 x nil))))
)
(define-fun lemma_I_14 ((x Int) (nil Int)) Int
(ite lemma_b79 
 (lemma_I1_48 x nil) 
 (ite lemma_b80 
 (nxt (lemma_I1_49 x nil)) 
 (prv (lemma_I1_50 x nil))))
)
(define-fun lemma_I_13 ((x Int) (nil Int)) Int
(ite lemma_b81 
 (lemma_I1_51 x nil) 
 (ite lemma_b82 
 (nxt (lemma_I1_52 x nil)) 
 (prv (lemma_I1_53 x nil))))
)
(define-fun lemma_I_15 ((x Int) (nil Int)) Int
(ite lemma_b84 
 (lemma_I1_54 x nil) 
 (ite lemma_b85 
 (nxt (lemma_I1_55 x nil)) 
 (prv (lemma_I1_56 x nil))))
)
(define-fun lemma_I_20 ((x Int) (nil Int)) Int
(ite lemma_b91 
 (lemma_I1_57 x nil) 
 (ite lemma_b92 
 (nxt (lemma_I1_58 x nil)) 
 (prv (lemma_I1_59 x nil))))
)
(define-fun lemma_I_18 ((x Int) (nil Int)) Int
(ite lemma_b98 
 (lemma_I1_60 x nil) 
 (ite lemma_b99 
 (nxt (lemma_I1_61 x nil)) 
 (prv (lemma_I1_62 x nil))))
)
(define-fun lemma_I_22 ((x Int) (nil Int)) Int
(ite lemma_b102 
 (lemma_I1_63 x nil) 
 (ite lemma_b103 
 (nxt (lemma_I1_64 x nil)) 
 (prv (lemma_I1_65 x nil))))
)
(define-fun lemma_I_23 ((x Int) (nil Int)) Int
(ite lemma_b112 
 (lemma_I1_66 x nil) 
 (ite lemma_b113 
 (nxt (lemma_I1_67 x nil)) 
 (prv (lemma_I1_68 x nil))))
)
(define-fun lemma_I_21 ((x Int) (nil Int)) Int
(ite lemma_b115 
 (lemma_I1_69 x nil) 
 (ite lemma_b116 
 (nxt (lemma_I1_70 x nil)) 
 (prv (lemma_I1_71 x nil))))
)
;Functions corresponding to B1
(define-fun lemma_B1_2 ((x Int) (nil Int)) Bool
(ite lemma_b4 
 (dlst (lemma_I_0 x nil)) 
 (ite lemma_b5 
 (slst (lemma_I_1 x nil)) 
 (sdlst (lemma_I_2 x nil))))
)
(define-fun lemma_B1_5 ((x Int) (nil Int)) Bool
(ite lemma_b6 
 (dlst (lemma_I_3 x nil)) 
 (ite lemma_b7 
 (slst (lemma_I_4 x nil)) 
 (sdlst (lemma_I_5 x nil))))
)
(define-fun lemma_B1_3 ((x Int) (nil Int)) Bool
(ite lemma_b8 
 (dlst (lemma_I_6 x nil)) 
 (ite lemma_b9 
 (slst (lemma_I_7 x nil)) 
 (sdlst (lemma_I_8 x nil))))
)
(define-fun lemma_B1_7 ((x Int) (nil Int)) Bool
(ite lemma_b23 
 (dlst (lemma_I_9 x nil)) 
 (ite lemma_b24 
 (slst (lemma_I_10 x nil)) 
 (sdlst (lemma_I_11 x nil))))
)
(define-fun lemma_B1_4 ((x Int) (nil Int)) Bool
(ite lemma_b26 
 (dlst (lemma_I_12 x nil)) 
 (ite lemma_b27 
 (slst (lemma_I_13 x nil)) 
 (sdlst (lemma_I_14 x nil))))
)
(define-fun lemma_B1_6 ((x Int) (nil Int)) Bool
(ite lemma_b31 
 (dlst (lemma_I_15 x nil)) 
 (ite lemma_b32 
 (slst (lemma_I_16 x nil)) 
 (sdlst (lemma_I_17 x nil))))
)
(define-fun lemma_B1_0 ((x Int) (nil Int)) Bool
(ite lemma_b38 
 (dlst (lemma_I_18 x nil)) 
 (ite lemma_b39 
 (slst (lemma_I_19 x nil)) 
 (sdlst (lemma_I_20 x nil))))
)
(define-fun lemma_B1_1 ((x Int) (nil Int)) Bool
(ite lemma_b40 
 (dlst (lemma_I_21 x nil)) 
 (ite lemma_b41 
 (slst (lemma_I_22 x nil)) 
 (sdlst (lemma_I_23 x nil))))
)
;Functions corresponding to Start
(define-fun lemma_Start_0 ((x Int) (nil Int)) Bool
(ite lemma_b0 
 (lemma_B1_0 x nil) 
 (ite lemma_b1 
 (=> (lemma_B1_1 x nil) (lemma_B1_1 x nil)) 
 (ite lemma_b2 
 (and (lemma_B1_3 x nil) (lemma_B1_3 x nil)) 
 (ite lemma_b3 
 (or (lemma_B1_5 x nil) (lemma_B1_5 x nil)) 
 (not (lemma_B1_7 x nil))))))
)

;Function to be synthesised
(define-fun lemma ((x Int) (nil Int)) Bool
(lemma_Start_0 x nil)
)


;Declaring boolean variables to encode grammar
(declare-const rswitch_b0 Bool)
(declare-const rswitch_b1 Bool)

;Declaring functions corresponding to nonterminals
;Functions corresponding to Start
(define-fun rswitch_Start_0 () Int
(ite rswitch_b0 
 0 
 (ite rswitch_b1 
 1 
 2))
)

;Function to be synthesised
(define-fun rswitch () Int
rswitch_Start_0
)

;; pfp constraints from counterexample models


;; constraints from false model
(assert (or (and (=> (= rswitch 0) (not (=> (dlst 1) (lemma 1 2))))
(=> (= rswitch 1) (not (=> (sdlst 1) (lemma 1 2))))
(=> (= rswitch 2) (not (=> (slst 1) (lemma 1 2))))
)
(and (=> (= rswitch 0) (not (=> (dlst 2) (lemma 2 2))))
(=> (= rswitch 1) (not (=> (sdlst 2) (lemma 2 2))))
(=> (= rswitch 2) (not (=> (slst 2) (lemma 2 2))))
)
(and (=> (= rswitch 0) (not (=> (dlst 3) (lemma 3 2))))
(=> (= rswitch 1) (not (=> (sdlst 3) (lemma 3 2))))
(=> (= rswitch 2) (not (=> (slst 3) (lemma 3 2))))
)
(and (=> (= rswitch 0) (not (=> (dlst 4) (lemma 4 2))))
(=> (= rswitch 1) (not (=> (sdlst 4) (lemma 4 2))))
(=> (= rswitch 2) (not (=> (slst 4) (lemma 4 2))))
)
))

;; constraints from true models

(check-sat)(get-model)