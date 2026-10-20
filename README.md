# forja-ide-runtime

Paquetes que Forja IDE descarga la primera vez para compilar con Gradle en el teléfono.

- `jdk17-<abi>.tar.xz`: OpenJDK 17 de Termux (GPLv2 + Classpath Exception) con sus librerías.
- `sdk36-<abi>.tar.xz`: android.jar API 36, build-tools 35.0.0 (jars) y aapt2/aidl/zipalign estáticos de lzhiyong/android-sdk-tools (Apache-2.0).
- `proot-<abi>.tar.xz`: proot de Termux (GPLv2), para C# sin conexión.
- `kotlinc-2.0.21.tar.xz`: kotlin-compiler-embeddable y dependencias (Apache-2.0).

Generado con `build_rt.py` desde packages.termux.dev.
