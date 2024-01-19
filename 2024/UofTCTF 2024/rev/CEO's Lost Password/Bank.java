import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.Map;

public class Bank {
    private static int a;
  
    private static long[] b = new long[13];

    static String a(String paramString) {
    byte[] arrayOfByte = paramString.getBytes(StandardCharsets.UTF_8);
    int i = (int)b[0] ^ 0x7EAEF08A;
    label15: while (i <= paramString.length()) {
      int j = (int)b[1] ^ 0x12DAB99D;
      while (j < arrayOfByte.length) {
        arrayOfByte[j] = (byte)(arrayOfByte[j] + (i - ((int)b[2] ^ 0x133C4920)) * j + ((int)b[3] ^ 0x6C4FFC99));
        j++;
        a = (int)b[4] ^ 0x724146AC;
        if ((a * a + a + ((int)b[5] ^ 0x520626FA)) % ((int)b[6] ^ 0x5B96E396) == 0);

      } 

      while (true) {
        i++;
        a = (int)b[7] ^ 0x39C3A44C;
        if ((a * a + a + ((int)b[5] ^ 0x520626FA)) % ((int)b[6] ^ 0x5B96E396) == 0)
          continue; 
        continue label15;
      } 
    } 

    return new String(Base64.getEncoder().encode(arrayOfByte), StandardCharsets.UTF_16);
  }

    public static void main(String[] param) {
        System.out.println(bb("\ucc02\ucc04\ucc12\ucc05"));
        System.out.println(bb("\ucc16\ucc13\ucc1a\ucc1e\ucc19"));
        Map<String, a> map = Map.of(b("\ucc02\ucc04\ucc12\ucc05"), new a(b("\ua645\ua315\ufb40\ubc5c\u9c00\uf14a"), 10.0F), b("\ucc16\ucc13\ucc1a\ucc1e\ucc19"), new a(b("\ub812\ue311\u8610\uf416\u9c47\u9a22\u9f21\u8b34\uaf3e\ufe3b\ua04f\ua905\ub903\ua50d\uba05\ua23d"), 100000.0F));
    }

    public static String bb(String paramString) {
        StringBuilder stringBuilder = new StringBuilder();
        int i = (int)b[1] ^ 0x12DAB99D;
        label10: while (i < paramString.length()) {
          char c = paramString.charAt(i);
          stringBuilder.append((char)((c ^ (int)b[10] ^ 0x20182D44) & 0xff));
          while (true) {
            i++;
            a = (int)b[11] ^ 0x418FE6B4;
            if ((a * a + a + ((int)b[5] ^ 0x520626FA)) % ((int)b[6] ^ 0x5B96E396) == 0)
                continue; 
            continue label10;
          } 
        } 
        return stringBuilder.toString();
      }

    public static String b(String paramString) {
        StringBuilder stringBuilder = new StringBuilder();
        int i = (int)b[1] ^ 0x12DAB99D;
        label10: while (i < paramString.length()) {
          char c = paramString.charAt(i);
          stringBuilder.append((char)((c ^ (int)b[10] ^ 0x20182D44)));
          while (true) {
            i++;
            a = (int)b[11] ^ 0x418FE6B4;
            if ((a * a + a + ((int)b[5] ^ 0x520626FA)) % ((int)b[6] ^ 0x5B96E396) == 0)
                continue; 
            continue label10;
          } 
        } 
        return stringBuilder.toString();
      }
      static {
        b[0] = 2125394059L;
        b[1] = 316324253L;
        b[2] = 322717996L;
        b[3] = 1817181343L;
        b[4] = 1916880576L;
        b[5] = 1376134909L;
        b[6] = 1536615367L;
        b[7] = 969122838L;
        b[8] = 935365158L;
        b[9] = 2029694981L;
        b[10] = 538501427L;
        b[11] = 1099949760L;
        b[12] = 977807481L;
        a = (int)b[12] ^ 0x44E6D8F3;
      }
}
