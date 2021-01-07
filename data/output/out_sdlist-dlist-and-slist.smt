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
(declare-const lemma_b140 Bool)
(declare-const lemma_b141 Bool)
(declare-const lemma_b142 Bool)
(declare-const lemma_b143 Bool)
(declare-const lemma_b144 Bool)
(declare-const lemma_b145 Bool)
(declare-const lemma_b146 Bool)
(declare-const lemma_b147 Bool)
(declare-const lemma_b148 Bool)
(declare-const lemma_b149 Bool)
(declare-const lemma_b150 Bool)
(declare-const lemma_b151 Bool)
(declare-const lemma_b152 Bool)
(declare-const lemma_b153 Bool)
(declare-const lemma_b154 Bool)
(declare-const lemma_b155 Bool)
(declare-const lemma_b156 Bool)
(declare-const lemma_b157 Bool)
(declare-const lemma_b158 Bool)
(declare-const lemma_b159 Bool)
(declare-const lemma_b160 Bool)
(declare-const lemma_b161 Bool)
(declare-const lemma_b162 Bool)
(declare-const lemma_b163 Bool)
(declare-const lemma_b164 Bool)
(declare-const lemma_b165 Bool)
(declare-const lemma_b166 Bool)
(declare-const lemma_b167 Bool)
(declare-const lemma_b168 Bool)
(declare-const lemma_b169 Bool)
(declare-const lemma_b170 Bool)
(declare-const lemma_b171 Bool)
(declare-const lemma_b172 Bool)
(declare-const lemma_b173 Bool)
(declare-const lemma_b174 Bool)
(declare-const lemma_b175 Bool)
(declare-const lemma_b176 Bool)
(declare-const lemma_b177 Bool)
(declare-const lemma_b178 Bool)
(declare-const lemma_b179 Bool)
(declare-const lemma_b180 Bool)
(declare-const lemma_b181 Bool)
(declare-const lemma_b182 Bool)
(declare-const lemma_b183 Bool)
(declare-const lemma_b184 Bool)
(declare-const lemma_b185 Bool)
(declare-const lemma_b186 Bool)
(declare-const lemma_b187 Bool)
(declare-const lemma_b188 Bool)
(declare-const lemma_b189 Bool)
(declare-const lemma_b190 Bool)
(declare-const lemma_b191 Bool)
(declare-const lemma_b192 Bool)
(declare-const lemma_b193 Bool)
(declare-const lemma_b194 Bool)
(declare-const lemma_b195 Bool)
(declare-const lemma_b196 Bool)
(declare-const lemma_b197 Bool)
(declare-const lemma_b198 Bool)
(declare-const lemma_b199 Bool)
(declare-const lemma_b200 Bool)
(declare-const lemma_b201 Bool)
(declare-const lemma_b202 Bool)
(declare-const lemma_b203 Bool)
(declare-const lemma_b204 Bool)
(declare-const lemma_b205 Bool)
(declare-const lemma_b206 Bool)
(declare-const lemma_b207 Bool)
(declare-const lemma_b208 Bool)
(declare-const lemma_b209 Bool)
(declare-const lemma_b210 Bool)
(declare-const lemma_b211 Bool)
(declare-const lemma_b212 Bool)
(declare-const lemma_b213 Bool)
(declare-const lemma_b214 Bool)
(declare-const lemma_b215 Bool)
(declare-const lemma_b216 Bool)
(declare-const lemma_b217 Bool)
(declare-const lemma_b218 Bool)
(declare-const lemma_b219 Bool)
(declare-const lemma_b220 Bool)
(declare-const lemma_b221 Bool)
(declare-const lemma_b222 Bool)
(declare-const lemma_b223 Bool)
(declare-const lemma_b224 Bool)
(declare-const lemma_b225 Bool)
(declare-const lemma_b226 Bool)
(declare-const lemma_b227 Bool)
(declare-const lemma_b228 Bool)
(declare-const lemma_b229 Bool)
(declare-const lemma_b230 Bool)
(declare-const lemma_b231 Bool)
(declare-const lemma_b232 Bool)
(declare-const lemma_b233 Bool)
(declare-const lemma_b234 Bool)
(declare-const lemma_b235 Bool)
(declare-const lemma_b236 Bool)
(declare-const lemma_b237 Bool)
(declare-const lemma_b238 Bool)
(declare-const lemma_b239 Bool)
(declare-const lemma_b240 Bool)
(declare-const lemma_b241 Bool)
(declare-const lemma_b242 Bool)
(declare-const lemma_b243 Bool)
(declare-const lemma_b244 Bool)

;Declaring functions corresponding to nonterminals
;Functions corresponding to I1
(define-fun lemma_I1_1 ((x Int) (nil Int)) Int
(ite lemma_b17 
 x 
 (ite lemma_b18 
 nil 
 nil))
)
(define-fun lemma_I1_3 ((x Int) (nil Int)) Int
(ite lemma_b40 
 x 
 (ite lemma_b41 
 nil 
 nil))
)
(define-fun lemma_I1_2 ((x Int) (nil Int)) Int
(ite lemma_b42 
 x 
 (ite lemma_b43 
 nil 
 nil))
)
(define-fun lemma_I1_5 ((x Int) (nil Int)) Int
(ite lemma_b44 
 x 
 (ite lemma_b45 
 nil 
 nil))
)
(define-fun lemma_I1_6 ((x Int) (nil Int)) Int
(ite lemma_b46 
 x 
 (ite lemma_b47 
 nil 
 nil))
)
(define-fun lemma_I1_9 ((x Int) (nil Int)) Int
(ite lemma_b48 
 x 
 (ite lemma_b49 
 nil 
 nil))
)
(define-fun lemma_I1_7 ((x Int) (nil Int)) Int
(ite lemma_b50 
 x 
 (ite lemma_b51 
 nil 
 nil))
)
(define-fun lemma_I1_14 ((x Int) (nil Int)) Int
(ite lemma_b55 
 x 
 (ite lemma_b56 
 nil 
 nil))
)
(define-fun lemma_I1_17 ((x Int) (nil Int)) Int
(ite lemma_b63 
 x 
 (ite lemma_b64 
 nil 
 nil))
)
(define-fun lemma_I1_20 ((x Int) (nil Int)) Int
(ite lemma_b65 
 x 
 (ite lemma_b66 
 nil 
 nil))
)
(define-fun lemma_I1_4 ((x Int) (nil Int)) Int
(ite lemma_b70 
 x 
 (ite lemma_b71 
 nil 
 nil))
)
(define-fun lemma_I1_0 ((x Int) (nil Int)) Int
(ite lemma_b78 
 x 
 (ite lemma_b79 
 nil 
 nil))
)
(define-fun lemma_I1_19 ((x Int) (nil Int)) Int
(ite lemma_b80 
 x 
 (ite lemma_b81 
 nil 
 nil))
)
(define-fun lemma_I1_11 ((x Int) (nil Int)) Int
(ite lemma_b85 
 x 
 (ite lemma_b86 
 nil 
 nil))
)
(define-fun lemma_I1_34 ((x Int) (nil Int)) Int
(ite lemma_b96 
 x 
 (ite lemma_b97 
 nil 
 nil))
)
(define-fun lemma_I1_13 ((x Int) (nil Int)) Int
(ite lemma_b98 
 x 
 (ite lemma_b99 
 nil 
 nil))
)
(define-fun lemma_I1_24 ((x Int) (nil Int)) Int
(ite lemma_b100 
 x 
 (ite lemma_b101 
 nil 
 nil))
)
(define-fun lemma_I1_10 ((x Int) (nil Int)) Int
(ite lemma_b102 
 x 
 (ite lemma_b103 
 nil 
 nil))
)
(define-fun lemma_I1_31 ((x Int) (nil Int)) Int
(ite lemma_b107 
 x 
 (ite lemma_b108 
 nil 
 nil))
)
(define-fun lemma_I1_41 ((x Int) (nil Int)) Int
(ite lemma_b109 
 x 
 (ite lemma_b110 
 nil 
 nil))
)
(define-fun lemma_I1_40 ((x Int) (nil Int)) Int
(ite lemma_b114 
 x 
 (ite lemma_b115 
 nil 
 nil))
)
(define-fun lemma_I1_30 ((x Int) (nil Int)) Int
(ite lemma_b116 
 x 
 (ite lemma_b117 
 nil 
 nil))
)
(define-fun lemma_I1_22 ((x Int) (nil Int)) Int
(ite lemma_b118 
 x 
 (ite lemma_b119 
 nil 
 nil))
)
(define-fun lemma_I1_36 ((x Int) (nil Int)) Int
(ite lemma_b123 
 x 
 (ite lemma_b124 
 nil 
 nil))
)
(define-fun lemma_I1_43 ((x Int) (nil Int)) Int
(ite lemma_b125 
 x 
 (ite lemma_b126 
 nil 
 nil))
)
(define-fun lemma_I1_33 ((x Int) (nil Int)) Int
(ite lemma_b127 
 x 
 (ite lemma_b128 
 nil 
 nil))
)
(define-fun lemma_I1_8 ((x Int) (nil Int)) Int
(ite lemma_b132 
 x 
 (ite lemma_b133 
 nil 
 nil))
)
(define-fun lemma_I1_28 ((x Int) (nil Int)) Int
(ite lemma_b134 
 x 
 (ite lemma_b135 
 nil 
 nil))
)
(define-fun lemma_I1_29 ((x Int) (nil Int)) Int
(ite lemma_b136 
 x 
 (ite lemma_b137 
 nil 
 nil))
)
(define-fun lemma_I1_15 ((x Int) (nil Int)) Int
(ite lemma_b138 
 x 
 (ite lemma_b139 
 nil 
 nil))
)
(define-fun lemma_I1_16 ((x Int) (nil Int)) Int
(ite lemma_b140 
 x 
 (ite lemma_b141 
 nil 
 nil))
)
(define-fun lemma_I1_18 ((x Int) (nil Int)) Int
(ite lemma_b148 
 x 
 (ite lemma_b149 
 nil 
 nil))
)
(define-fun lemma_I1_23 ((x Int) (nil Int)) Int
(ite lemma_b156 
 x 
 (ite lemma_b157 
 nil 
 nil))
)
(define-fun lemma_I1_56 ((x Int) (nil Int)) Int
(ite lemma_b158 
 x 
 (ite lemma_b159 
 nil 
 nil))
)
(define-fun lemma_I1_27 ((x Int) (nil Int)) Int
(ite lemma_b160 
 x 
 (ite lemma_b161 
 nil 
 nil))
)
(define-fun lemma_I1_32 ((x Int) (nil Int)) Int
(ite lemma_b162 
 x 
 (ite lemma_b163 
 nil 
 nil))
)
(define-fun lemma_I1_52 ((x Int) (nil Int)) Int
(ite lemma_b164 
 x 
 (ite lemma_b165 
 nil 
 nil))
)
(define-fun lemma_I1_35 ((x Int) (nil Int)) Int
(ite lemma_b169 
 x 
 (ite lemma_b170 
 nil 
 nil))
)
(define-fun lemma_I1_51 ((x Int) (nil Int)) Int
(ite lemma_b171 
 x 
 (ite lemma_b172 
 nil 
 nil))
)
(define-fun lemma_I1_55 ((x Int) (nil Int)) Int
(ite lemma_b173 
 x 
 (ite lemma_b174 
 nil 
 nil))
)
(define-fun lemma_I1_12 ((x Int) (nil Int)) Int
(ite lemma_b175 
 x 
 (ite lemma_b176 
 nil 
 nil))
)
(define-fun lemma_I1_39 ((x Int) (nil Int)) Int
(ite lemma_b180 
 x 
 (ite lemma_b181 
 nil 
 nil))
)
(define-fun lemma_I1_21 ((x Int) (nil Int)) Int
(ite lemma_b182 
 x 
 (ite lemma_b183 
 nil 
 nil))
)
(define-fun lemma_I1_26 ((x Int) (nil Int)) Int
(ite lemma_b184 
 x 
 (ite lemma_b185 
 nil 
 nil))
)
(define-fun lemma_I1_47 ((x Int) (nil Int)) Int
(ite lemma_b186 
 x 
 (ite lemma_b187 
 nil 
 nil))
)
(define-fun lemma_I1_25 ((x Int) (nil Int)) Int
(ite lemma_b188 
 x 
 (ite lemma_b189 
 nil 
 nil))
)
(define-fun lemma_I1_44 ((x Int) (nil Int)) Int
(ite lemma_b190 
 x 
 (ite lemma_b191 
 nil 
 nil))
)
(define-fun lemma_I1_67 ((x Int) (nil Int)) Int
(ite lemma_b192 
 x 
 (ite lemma_b193 
 nil 
 nil))
)
(define-fun lemma_I1_58 ((x Int) (nil Int)) Int
(ite lemma_b194 
 x 
 (ite lemma_b195 
 nil 
 nil))
)
(define-fun lemma_I1_53 ((x Int) (nil Int)) Int
(ite lemma_b199 
 x 
 (ite lemma_b200 
 nil 
 nil))
)
(define-fun lemma_I1_42 ((x Int) (nil Int)) Int
(ite lemma_b201 
 x 
 (ite lemma_b202 
 nil 
 nil))
)
(define-fun lemma_I1_57 ((x Int) (nil Int)) Int
(ite lemma_b203 
 x 
 (ite lemma_b204 
 nil 
 nil))
)
(define-fun lemma_I1_37 ((x Int) (nil Int)) Int
(ite lemma_b205 
 x 
 (ite lemma_b206 
 nil 
 nil))
)
(define-fun lemma_I1_46 ((x Int) (nil Int)) Int
(ite lemma_b207 
 x 
 (ite lemma_b208 
 nil 
 nil))
)
(define-fun lemma_I1_50 ((x Int) (nil Int)) Int
(ite lemma_b209 
 x 
 (ite lemma_b210 
 nil 
 nil))
)
(define-fun lemma_I1_54 ((x Int) (nil Int)) Int
(ite lemma_b211 
 x 
 (ite lemma_b212 
 nil 
 nil))
)
(define-fun lemma_I1_38 ((x Int) (nil Int)) Int
(ite lemma_b213 
 x 
 (ite lemma_b214 
 nil 
 nil))
)
(define-fun lemma_I1_71 ((x Int) (nil Int)) Int
(ite lemma_b215 
 x 
 (ite lemma_b216 
 nil 
 nil))
)
(define-fun lemma_I1_69 ((x Int) (nil Int)) Int
(ite lemma_b217 
 x 
 (ite lemma_b218 
 nil 
 nil))
)
(define-fun lemma_I1_62 ((x Int) (nil Int)) Int
(ite lemma_b219 
 x 
 (ite lemma_b220 
 nil 
 nil))
)
(define-fun lemma_I1_61 ((x Int) (nil Int)) Int
(ite lemma_b221 
 x 
 (ite lemma_b222 
 nil 
 nil))
)
(define-fun lemma_I1_48 ((x Int) (nil Int)) Int
(ite lemma_b223 
 x 
 (ite lemma_b224 
 nil 
 nil))
)
(define-fun lemma_I1_64 ((x Int) (nil Int)) Int
(ite lemma_b225 
 x 
 (ite lemma_b226 
 nil 
 nil))
)
(define-fun lemma_I1_59 ((x Int) (nil Int)) Int
(ite lemma_b227 
 x 
 (ite lemma_b228 
 nil 
 nil))
)
(define-fun lemma_I1_45 ((x Int) (nil Int)) Int
(ite lemma_b229 
 x 
 (ite lemma_b230 
 nil 
 nil))
)
(define-fun lemma_I1_49 ((x Int) (nil Int)) Int
(ite lemma_b231 
 x 
 (ite lemma_b232 
 nil 
 nil))
)
(define-fun lemma_I1_70 ((x Int) (nil Int)) Int
(ite lemma_b233 
 x 
 (ite lemma_b234 
 nil 
 nil))
)
(define-fun lemma_I1_60 ((x Int) (nil Int)) Int
(ite lemma_b235 
 x 
 (ite lemma_b236 
 nil 
 nil))
)
(define-fun lemma_I1_68 ((x Int) (nil Int)) Int
(ite lemma_b237 
 x 
 (ite lemma_b238 
 nil 
 nil))
)
(define-fun lemma_I1_65 ((x Int) (nil Int)) Int
(ite lemma_b239 
 x 
 (ite lemma_b240 
 nil 
 nil))
)
(define-fun lemma_I1_66 ((x Int) (nil Int)) Int
(ite lemma_b241 
 x 
 (ite lemma_b242 
 nil 
 nil))
)
(define-fun lemma_I1_63 ((x Int) (nil Int)) Int
(ite lemma_b243 
 x 
 (ite lemma_b244 
 nil 
 nil))
)
;Functions corresponding to I
(define-fun lemma_I_2 ((x Int) (nil Int)) Int
(ite lemma_b8 
 (lemma_I1_0 x nil) 
 (ite lemma_b9 
 (nxt (lemma_I1_1 x nil)) 
 (ite lemma_b10 
 (prv (lemma_I1_2 x nil)) 
 (prv (lemma_I1_2 x nil)))))
)
(define-fun lemma_I_8 ((x Int) (nil Int)) Int
(ite lemma_b19 
 (lemma_I1_3 x nil) 
 (ite lemma_b20 
 (nxt (lemma_I1_4 x nil)) 
 (ite lemma_b21 
 (prv (lemma_I1_5 x nil)) 
 (prv (lemma_I1_5 x nil)))))
)
(define-fun lemma_I_6 ((x Int) (nil Int)) Int
(ite lemma_b22 
 (lemma_I1_6 x nil) 
 (ite lemma_b23 
 (nxt (lemma_I1_7 x nil)) 
 (ite lemma_b24 
 (prv (lemma_I1_8 x nil)) 
 (prv (lemma_I1_8 x nil)))))
)
(define-fun lemma_I_5 ((x Int) (nil Int)) Int
(ite lemma_b25 
 (lemma_I1_9 x nil) 
 (ite lemma_b26 
 (nxt (lemma_I1_10 x nil)) 
 (ite lemma_b27 
 (prv (lemma_I1_11 x nil)) 
 (prv (lemma_I1_11 x nil)))))
)
(define-fun lemma_I_3 ((x Int) (nil Int)) Int
(ite lemma_b34 
 (lemma_I1_12 x nil) 
 (ite lemma_b35 
 (nxt (lemma_I1_13 x nil)) 
 (ite lemma_b36 
 (prv (lemma_I1_14 x nil)) 
 (prv (lemma_I1_14 x nil)))))
)
(define-fun lemma_I_17 ((x Int) (nil Int)) Int
(ite lemma_b52 
 (lemma_I1_15 x nil) 
 (ite lemma_b53 
 (nxt (lemma_I1_16 x nil)) 
 (ite lemma_b54 
 (prv (lemma_I1_17 x nil)) 
 (prv (lemma_I1_17 x nil)))))
)
(define-fun lemma_I_4 ((x Int) (nil Int)) Int
(ite lemma_b57 
 (lemma_I1_18 x nil) 
 (ite lemma_b58 
 (nxt (lemma_I1_19 x nil)) 
 (ite lemma_b59 
 (prv (lemma_I1_20 x nil)) 
 (prv (lemma_I1_20 x nil)))))
)
(define-fun lemma_I_16 ((x Int) (nil Int)) Int
(ite lemma_b60 
 (lemma_I1_21 x nil) 
 (ite lemma_b61 
 (nxt (lemma_I1_22 x nil)) 
 (ite lemma_b62 
 (prv (lemma_I1_23 x nil)) 
 (prv (lemma_I1_23 x nil)))))
)
(define-fun lemma_I_15 ((x Int) (nil Int)) Int
(ite lemma_b67 
 (lemma_I1_24 x nil) 
 (ite lemma_b68 
 (nxt (lemma_I1_25 x nil)) 
 (ite lemma_b69 
 (prv (lemma_I1_26 x nil)) 
 (prv (lemma_I1_26 x nil)))))
)
(define-fun lemma_I_9 ((x Int) (nil Int)) Int
(ite lemma_b82 
 (lemma_I1_27 x nil) 
 (ite lemma_b83 
 (nxt (lemma_I1_28 x nil)) 
 (ite lemma_b84 
 (prv (lemma_I1_29 x nil)) 
 (prv (lemma_I1_29 x nil)))))
)
(define-fun lemma_I_7 ((x Int) (nil Int)) Int
(ite lemma_b87 
 (lemma_I1_30 x nil) 
 (ite lemma_b88 
 (nxt (lemma_I1_31 x nil)) 
 (ite lemma_b89 
 (prv (lemma_I1_32 x nil)) 
 (prv (lemma_I1_32 x nil)))))
)
(define-fun lemma_I_12 ((x Int) (nil Int)) Int
(ite lemma_b90 
 (lemma_I1_33 x nil) 
 (ite lemma_b91 
 (nxt (lemma_I1_34 x nil)) 
 (ite lemma_b92 
 (prv (lemma_I1_35 x nil)) 
 (prv (lemma_I1_35 x nil)))))
)
(define-fun lemma_I_22 ((x Int) (nil Int)) Int
(ite lemma_b93 
 (lemma_I1_36 x nil) 
 (ite lemma_b94 
 (nxt (lemma_I1_37 x nil)) 
 (ite lemma_b95 
 (prv (lemma_I1_38 x nil)) 
 (prv (lemma_I1_38 x nil)))))
)
(define-fun lemma_I_20 ((x Int) (nil Int)) Int
(ite lemma_b104 
 (lemma_I1_39 x nil) 
 (ite lemma_b105 
 (nxt (lemma_I1_40 x nil)) 
 (ite lemma_b106 
 (prv (lemma_I1_41 x nil)) 
 (prv (lemma_I1_41 x nil)))))
)
(define-fun lemma_I_18 ((x Int) (nil Int)) Int
(ite lemma_b111 
 (lemma_I1_42 x nil) 
 (ite lemma_b112 
 (nxt (lemma_I1_43 x nil)) 
 (ite lemma_b113 
 (prv (lemma_I1_44 x nil)) 
 (prv (lemma_I1_44 x nil)))))
)
(define-fun lemma_I_13 ((x Int) (nil Int)) Int
(ite lemma_b120 
 (lemma_I1_45 x nil) 
 (ite lemma_b121 
 (nxt (lemma_I1_46 x nil)) 
 (ite lemma_b122 
 (prv (lemma_I1_47 x nil)) 
 (prv (lemma_I1_47 x nil)))))
)
(define-fun lemma_I_1 ((x Int) (nil Int)) Int
(ite lemma_b129 
 (lemma_I1_48 x nil) 
 (ite lemma_b130 
 (nxt (lemma_I1_49 x nil)) 
 (ite lemma_b131 
 (prv (lemma_I1_50 x nil)) 
 (prv (lemma_I1_50 x nil)))))
)
(define-fun lemma_I_0 ((x Int) (nil Int)) Int
(ite lemma_b142 
 (lemma_I1_51 x nil) 
 (ite lemma_b143 
 (nxt (lemma_I1_52 x nil)) 
 (ite lemma_b144 
 (prv (lemma_I1_53 x nil)) 
 (prv (lemma_I1_53 x nil)))))
)
(define-fun lemma_I_19 ((x Int) (nil Int)) Int
(ite lemma_b145 
 (lemma_I1_54 x nil) 
 (ite lemma_b146 
 (nxt (lemma_I1_55 x nil)) 
 (ite lemma_b147 
 (prv (lemma_I1_56 x nil)) 
 (prv (lemma_I1_56 x nil)))))
)
(define-fun lemma_I_14 ((x Int) (nil Int)) Int
(ite lemma_b150 
 (lemma_I1_57 x nil) 
 (ite lemma_b151 
 (nxt (lemma_I1_58 x nil)) 
 (ite lemma_b152 
 (prv (lemma_I1_59 x nil)) 
 (prv (lemma_I1_59 x nil)))))
)
(define-fun lemma_I_10 ((x Int) (nil Int)) Int
(ite lemma_b153 
 (lemma_I1_60 x nil) 
 (ite lemma_b154 
 (nxt (lemma_I1_61 x nil)) 
 (ite lemma_b155 
 (prv (lemma_I1_62 x nil)) 
 (prv (lemma_I1_62 x nil)))))
)
(define-fun lemma_I_21 ((x Int) (nil Int)) Int
(ite lemma_b166 
 (lemma_I1_63 x nil) 
 (ite lemma_b167 
 (nxt (lemma_I1_64 x nil)) 
 (ite lemma_b168 
 (prv (lemma_I1_65 x nil)) 
 (prv (lemma_I1_65 x nil)))))
)
(define-fun lemma_I_11 ((x Int) (nil Int)) Int
(ite lemma_b177 
 (lemma_I1_66 x nil) 
 (ite lemma_b178 
 (nxt (lemma_I1_67 x nil)) 
 (ite lemma_b179 
 (prv (lemma_I1_68 x nil)) 
 (prv (lemma_I1_68 x nil)))))
)
(define-fun lemma_I_23 ((x Int) (nil Int)) Int
(ite lemma_b196 
 (lemma_I1_69 x nil) 
 (ite lemma_b197 
 (nxt (lemma_I1_70 x nil)) 
 (ite lemma_b198 
 (prv (lemma_I1_71 x nil)) 
 (prv (lemma_I1_71 x nil)))))
)
;Functions corresponding to B1
(define-fun lemma_B1_0 ((x Int) (nil Int)) Bool
(ite lemma_b5 
 (dlst (lemma_I_0 x nil)) 
 (ite lemma_b6 
 (slst (lemma_I_1 x nil)) 
 (ite lemma_b7 
 (sdlst (lemma_I_2 x nil)) 
 (sdlst (lemma_I_2 x nil)))))
)
(define-fun lemma_B1_3 ((x Int) (nil Int)) Bool
(ite lemma_b11 
 (dlst (lemma_I_3 x nil)) 
 (ite lemma_b12 
 (slst (lemma_I_4 x nil)) 
 (ite lemma_b13 
 (sdlst (lemma_I_5 x nil)) 
 (sdlst (lemma_I_5 x nil)))))
)
(define-fun lemma_B1_1 ((x Int) (nil Int)) Bool
(ite lemma_b14 
 (dlst (lemma_I_6 x nil)) 
 (ite lemma_b15 
 (slst (lemma_I_7 x nil)) 
 (ite lemma_b16 
 (sdlst (lemma_I_8 x nil)) 
 (sdlst (lemma_I_8 x nil)))))
)
(define-fun lemma_B1_6 ((x Int) (nil Int)) Bool
(ite lemma_b28 
 (dlst (lemma_I_9 x nil)) 
 (ite lemma_b29 
 (slst (lemma_I_10 x nil)) 
 (ite lemma_b30 
 (sdlst (lemma_I_11 x nil)) 
 (sdlst (lemma_I_11 x nil)))))
)
(define-fun lemma_B1_5 ((x Int) (nil Int)) Bool
(ite lemma_b31 
 (dlst (lemma_I_12 x nil)) 
 (ite lemma_b32 
 (slst (lemma_I_13 x nil)) 
 (ite lemma_b33 
 (sdlst (lemma_I_14 x nil)) 
 (sdlst (lemma_I_14 x nil)))))
)
(define-fun lemma_B1_4 ((x Int) (nil Int)) Bool
(ite lemma_b37 
 (dlst (lemma_I_15 x nil)) 
 (ite lemma_b38 
 (slst (lemma_I_16 x nil)) 
 (ite lemma_b39 
 (sdlst (lemma_I_17 x nil)) 
 (sdlst (lemma_I_17 x nil)))))
)
(define-fun lemma_B1_2 ((x Int) (nil Int)) Bool
(ite lemma_b72 
 (dlst (lemma_I_18 x nil)) 
 (ite lemma_b73 
 (slst (lemma_I_19 x nil)) 
 (ite lemma_b74 
 (sdlst (lemma_I_20 x nil)) 
 (sdlst (lemma_I_20 x nil)))))
)
(define-fun lemma_B1_7 ((x Int) (nil Int)) Bool
(ite lemma_b75 
 (dlst (lemma_I_21 x nil)) 
 (ite lemma_b76 
 (slst (lemma_I_22 x nil)) 
 (ite lemma_b77 
 (sdlst (lemma_I_23 x nil)) 
 (sdlst (lemma_I_23 x nil)))))
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
 (ite lemma_b4 
 (not (lemma_B1_7 x nil)) 
 (not (lemma_B1_7 x nil)))))))
)

;Asserting affirmative choice of some boolean variable for each function
(assert (or lemma_b17 lemma_b18))
(assert (or lemma_b40 lemma_b41))
(assert (or lemma_b42 lemma_b43))
(assert (or lemma_b44 lemma_b45))
(assert (or lemma_b46 lemma_b47))
(assert (or lemma_b48 lemma_b49))
(assert (or lemma_b50 lemma_b51))
(assert (or lemma_b55 lemma_b56))
(assert (or lemma_b63 lemma_b64))
(assert (or lemma_b65 lemma_b66))
(assert (or lemma_b70 lemma_b71))
(assert (or lemma_b78 lemma_b79))
(assert (or lemma_b80 lemma_b81))
(assert (or lemma_b85 lemma_b86))
(assert (or lemma_b96 lemma_b97))
(assert (or lemma_b98 lemma_b99))
(assert (or lemma_b100 lemma_b101))
(assert (or lemma_b102 lemma_b103))
(assert (or lemma_b107 lemma_b108))
(assert (or lemma_b109 lemma_b110))
(assert (or lemma_b114 lemma_b115))
(assert (or lemma_b116 lemma_b117))
(assert (or lemma_b118 lemma_b119))
(assert (or lemma_b123 lemma_b124))
(assert (or lemma_b125 lemma_b126))
(assert (or lemma_b127 lemma_b128))
(assert (or lemma_b132 lemma_b133))
(assert (or lemma_b134 lemma_b135))
(assert (or lemma_b136 lemma_b137))
(assert (or lemma_b138 lemma_b139))
(assert (or lemma_b140 lemma_b141))
(assert (or lemma_b148 lemma_b149))
(assert (or lemma_b156 lemma_b157))
(assert (or lemma_b158 lemma_b159))
(assert (or lemma_b160 lemma_b161))
(assert (or lemma_b162 lemma_b163))
(assert (or lemma_b164 lemma_b165))
(assert (or lemma_b169 lemma_b170))
(assert (or lemma_b171 lemma_b172))
(assert (or lemma_b173 lemma_b174))
(assert (or lemma_b175 lemma_b176))
(assert (or lemma_b180 lemma_b181))
(assert (or lemma_b182 lemma_b183))
(assert (or lemma_b184 lemma_b185))
(assert (or lemma_b186 lemma_b187))
(assert (or lemma_b188 lemma_b189))
(assert (or lemma_b190 lemma_b191))
(assert (or lemma_b192 lemma_b193))
(assert (or lemma_b194 lemma_b195))
(assert (or lemma_b199 lemma_b200))
(assert (or lemma_b201 lemma_b202))
(assert (or lemma_b203 lemma_b204))
(assert (or lemma_b205 lemma_b206))
(assert (or lemma_b207 lemma_b208))
(assert (or lemma_b209 lemma_b210))
(assert (or lemma_b211 lemma_b212))
(assert (or lemma_b213 lemma_b214))
(assert (or lemma_b215 lemma_b216))
(assert (or lemma_b217 lemma_b218))
(assert (or lemma_b219 lemma_b220))
(assert (or lemma_b221 lemma_b222))
(assert (or lemma_b223 lemma_b224))
(assert (or lemma_b225 lemma_b226))
(assert (or lemma_b227 lemma_b228))
(assert (or lemma_b229 lemma_b230))
(assert (or lemma_b231 lemma_b232))
(assert (or lemma_b233 lemma_b234))
(assert (or lemma_b235 lemma_b236))
(assert (or lemma_b237 lemma_b238))
(assert (or lemma_b239 lemma_b240))
(assert (or lemma_b241 lemma_b242))
(assert (or lemma_b243 lemma_b244))
(assert (or lemma_b8 lemma_b9 lemma_b10))
(assert (or lemma_b19 lemma_b20 lemma_b21))
(assert (or lemma_b22 lemma_b23 lemma_b24))
(assert (or lemma_b25 lemma_b26 lemma_b27))
(assert (or lemma_b34 lemma_b35 lemma_b36))
(assert (or lemma_b52 lemma_b53 lemma_b54))
(assert (or lemma_b57 lemma_b58 lemma_b59))
(assert (or lemma_b60 lemma_b61 lemma_b62))
(assert (or lemma_b67 lemma_b68 lemma_b69))
(assert (or lemma_b82 lemma_b83 lemma_b84))
(assert (or lemma_b87 lemma_b88 lemma_b89))
(assert (or lemma_b90 lemma_b91 lemma_b92))
(assert (or lemma_b93 lemma_b94 lemma_b95))
(assert (or lemma_b104 lemma_b105 lemma_b106))
(assert (or lemma_b111 lemma_b112 lemma_b113))
(assert (or lemma_b120 lemma_b121 lemma_b122))
(assert (or lemma_b129 lemma_b130 lemma_b131))
(assert (or lemma_b142 lemma_b143 lemma_b144))
(assert (or lemma_b145 lemma_b146 lemma_b147))
(assert (or lemma_b150 lemma_b151 lemma_b152))
(assert (or lemma_b153 lemma_b154 lemma_b155))
(assert (or lemma_b166 lemma_b167 lemma_b168))
(assert (or lemma_b177 lemma_b178 lemma_b179))
(assert (or lemma_b196 lemma_b197 lemma_b198))
(assert (or lemma_b5 lemma_b6 lemma_b7))
(assert (or lemma_b11 lemma_b12 lemma_b13))
(assert (or lemma_b14 lemma_b15 lemma_b16))
(assert (or lemma_b28 lemma_b29 lemma_b30))
(assert (or lemma_b31 lemma_b32 lemma_b33))
(assert (or lemma_b37 lemma_b38 lemma_b39))
(assert (or lemma_b72 lemma_b73 lemma_b74))
(assert (or lemma_b75 lemma_b76 lemma_b77))
(assert (or lemma_b0 lemma_b1 lemma_b2 lemma_b3 lemma_b4))

;Function to be synthesised
(define-fun lemma ((x Int) (nil Int)) Bool
(lemma_Start_0 x nil)
)


;Declaring boolean variables to encode grammar
(declare-const rswitch_b0 Bool)
(declare-const rswitch_b1 Bool)
(declare-const rswitch_b2 Bool)

;Declaring functions corresponding to nonterminals
;Functions corresponding to Start
(define-fun rswitch_Start_0 () Int
(ite rswitch_b0 
 0 
 (ite rswitch_b1 
 1 
 (ite rswitch_b2 
 2 
 2)))
)

;Asserting affirmative choice of some boolean variable for each function
(assert (or rswitch_b0 rswitch_b1 rswitch_b2))

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