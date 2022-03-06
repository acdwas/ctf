
// https://golangdocs.com/aes-encryption-decryption-in-golang

package main

import (
	"crypto/aes"
	"encoding/hex"
	"fmt"
)

func main() {

	// cipher key
	key := "EYF45#NDJFJ^DSHSKhdh53728#cksa08"

	// plaintext
	pt := "This is a secret"

	// c := EncryptAES([]byte(key), pt)
	// c := "7fcaed77d5a13eb8de8828f17e840b0fb9c05599e0917bce625c4741e32da751"

	c0 := "12f8fde4ffe8bbf0e6044b6d04423ebf"
	c1 := "ac6a90115534fadace815350f28420b6"

	// plaintext
	fmt.Println(pt)

	// ciphertext
	fmt.Println(c0)

	// decrypt
	DecryptAES([]byte(key), c0)

	// plaintext
	fmt.Println(pt)

	// ciphertext
	fmt.Println(c1)

	// decrypt
	DecryptAES([]byte(key), c1)

}

func EncryptAES(key []byte, plaintext string) string {

	c, err := aes.NewCipher(key)
	CheckError(err)

	out := make([]byte, len(plaintext))

	c.Encrypt(out, []byte(plaintext))

	return hex.EncodeToString(out)
}

func DecryptAES(key []byte, ct string) {
	ciphertext, _ := hex.DecodeString(ct)

	c, err := aes.NewCipher(key)
	CheckError(err)

	pt := make([]byte, len(ciphertext))
	c.Decrypt(pt, ciphertext)

	s := string(pt[:])
	fmt.Println("DECRYPTED:", s)
}

func CheckError(err error) {
	if err != nil {
		panic(err)
	}
}

// GLUG{G0oo_b1n4r1Es_ar3_fuN_4563}

