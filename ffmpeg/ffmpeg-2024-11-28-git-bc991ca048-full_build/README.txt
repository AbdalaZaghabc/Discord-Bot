FFmpeg 64-bit static Windows build from www.gyan.dev

Version: 2024-11-28-git-bc991ca048-full_build-www.gyan.dev

License: GPL v3

Source Code: https://github.com/FFmpeg/FFmpeg/commit/bc991ca048

External Assets
frei0r plugins:   https://www.gyan.dev/ffmpeg/builds/ffmpeg-frei0r-plugins
lensfun database: https://www.gyan.dev/ffmpeg/builds/ffmpeg-lensfun-db

git-full build configuration: 

ARCH                      x86 (generic)
big-endian                no
runtime cpu detection     yes
standalone assembly       yes
x86 assembler             nasm
MMX enabled               yes
MMXEXT enabled            yes
3DNow! enabled            yes
3DNow! extended enabled   yes
SSE enabled               yes
SSSE3 enabled             yes
AESNI enabled             yes
AVX enabled               yes
AVX2 enabled              yes
AVX-512 enabled           yes
AVX-512ICL enabled        yes
XOP enabled               yes
FMA3 enabled              yes
FMA4 enabled              yes
i686 features enabled     yes
CMOV is fast              yes
EBX available             yes
EBP available             yes
debug symbols             yes
strip symbols             yes
optimize for size         no
optimizations             yes
static                    yes
shared                    no
postprocessing support    yes
network support           yes
threading support         pthreads
safe bitstream reader     yes
texi2html enabled         no
perl enabled              yes
pod2man enabled           yes
makeinfo enabled          yes
makeinfo supports HTML    yes
xmllint enabled           yes

External libraries:
avisynth                libilbc                 libtheora
bzlib                   libjxl                  libtwolame
chromaprint             liblc3                  libuavs3d
frei0r                  liblensfun              libvidstab
gmp                     libmodplug              libvmaf
gnutls                  libmp3lame              libvo_amrwbenc
iconv                   libmysofa               libvorbis
ladspa                  libopencore_amrnb       libvpx
libaom                  libopencore_amrwb       libvvenc
libaribb24              libopenjpeg             libwebp
libaribcaption          libopenmpt              libx264
libass                  libopus                 libx265
libbluray               libplacebo              libxavs2
libbs2b                 libqrencode             libxevd
libcaca                 libquirc                libxeve
libcdio                 librav1e                libxml2
libcodec2               librist                 libxvid
libdav1d                librubberband           libzimg
libdavs2                libshaderc              libzmq
libflite                libshine                libzvbi
libfontconfig           libsnappy               lzma
libfreetype             libsoxr                 mediafoundation
libfribidi              libspeex                sdl2
libgme                  libsrt                  zlib
libgsm                  libssh
libharfbuzz             libsvtav1

External libraries providing hardware acceleration:
amf                     d3d12va                 nvdec
cuda                    dxva2                   nvenc
cuda_llvm               ffnvcodec               opencl
cuvid                   libmfx                  vaapi
d3d11va                 libvpl                  vulkan

Libraries:
avcodec                 avformat                swresample
avdevice                avutil                  swscale
avfilter                postproc

Programs:
ffmpeg                  ffplay                  ffprobe

Enabled decoders:
aac                     g723_1                  pcx
aac_fixed               g729                    pdv
aac_latm                gdv                     pfm
aasc                    gem                     pgm
ac3                     gif                     pgmyuv
ac3_fixed               gremlin_dpcm            pgssub
acelp_kelvin            gsm                     pgx
adpcm_4xm               gsm_ms                  phm
adpcm_adx               h261                    photocd
adpcm_afc               h263                    pictor
adpcm_agm               h263i                   pixlet
adpcm_aica              h263p                   pjs
adpcm_argo              h264                    png
adpcm_ct                h264_cuvid              ppm
adpcm_dtk               h264_qsv                prores
adpcm_ea                hap                     prosumer
adpcm_ea_maxis_xa       hca                     psd
adpcm_ea_r1             hcom                    ptx
adpcm_ea_r2             hdr                     qcelp
adpcm_ea_r3             hevc                    qdm2
adpcm_ea_xas            hevc_cuvid              qdmc
adpcm_g722              hevc_qsv                qdraw
adpcm_g726              hnm4_video              qoa
adpcm_g726le            hq_hqa                  qoi
adpcm_ima_acorn         hqx                     qpeg
adpcm_ima_alp           huffyuv                 qtrle
adpcm_ima_amv           hymt                    r10k
adpcm_ima_apc           iac                     r210
adpcm_ima_apm           idcin                   ra_144
adpcm_ima_cunning       idf                     ra_288
adpcm_ima_dat4          iff_ilbm                ralf
adpcm_ima_dk3           ilbc                    rasc
adpcm_ima_dk4           imc                     rawvideo
adpcm_ima_ea_eacs       imm4                    realtext
adpcm_ima_ea_sead       imm5                    rka
adpcm_ima_iss           indeo2                  rl2
adpcm_ima_moflex        indeo3                  roq
adpcm_ima_mtf           indeo4                  roq_dpcm
adpcm_ima_oki           indeo5                  rpza
adpcm_ima_qt            interplay_acm           rscc
adpcm_ima_rad           interplay_dpcm          rtv1
adpcm_ima_smjpeg        interplay_video         rv10
adpcm_ima_ssi           ipu                     rv20
adpcm_ima_wav           jacosub                 rv30
adpcm_ima_ws            jpeg2000                rv40
adpcm_ms                jpegls                  rv60
adpcm_mtaf              jv                      s302m
adpcm_psx               kgv1                    sami
adpcm_sbpro_2           kmvc                    sanm
adpcm_sbpro_3           lagarith                sbc
adpcm_sbpro_4           lead                    scpr
adpcm_swf               libaom_av1              screenpresso
adpcm_thp               libaribb24              sdx2_dpcm
adpcm_thp_le            libaribcaption          sga
adpcm_vima              libcodec2               sgi
adpcm_xa                libdav1d                sgirle
adpcm_xmd               libdavs2                sheervideo
adpcm_yamaha            libgsm                  shorten
adpcm_zork              libgsm_ms               simbiosis_imx
agm                     libilbc                 sipr
aic                     libjxl                  siren
alac                    liblc3                  smackaud
alias_pix               libopencore_amrnb       smacker
als                     libopencore_amrwb       smc
amrnb                   libopus                 smvjpeg
amrwb                   libspeex                snow
amv                     libuavs3d               sol_dpcm
anm                     libvorbis               sonic
ansi                    libvpx_vp8              sp5x
anull                   libvpx_vp9              speedhq
apac                    libxevd                 speex
ape                     libzvbi_teletext        srgc
apng                    loco                    srt
aptx                    lscr                    ssa
aptx_hd                 m101                    stl
arbc                    mace3                   subrip
argo                    mace6                   subviewer
ass                     magicyuv                subviewer1
asv1                    mdec                    sunrast
asv2                    media100                svq1
atrac1                  metasound               svq3
atrac3                  microdvd                tak
atrac3al                mimic                   targa
atrac3p                 misc4                   targa_y216
atrac3pal               mjpeg                   tdsc
atrac9                  mjpeg_cuvid             text
aura                    mjpeg_qsv               theora
aura2                   mjpegb                  thp
av1                     mlp                     tiertexseqvideo
av1_cuvid               mmvideo                 tiff
av1_qsv                 mobiclip                tmv
avrn                    motionpixels            truehd
avrp                    movtext                 truemotion1
avs                     mp1                     truemotion2
avui                    mp1float                truemotion2rt
bethsoftvid             mp2                     truespeech
bfi                     mp2float                tscc
bink                    mp3                     tscc2
binkaudio_dct           mp3adu                  tta
binkaudio_rdft          mp3adufloat             twinvq
bintext                 mp3float                txd
bitpacked               mp3on4                  ulti
bmp                     mp3on4float             utvideo
bmv_audio               mpc7                    v210
bmv_video               mpc8                    v210x
bonk                    mpeg1_cuvid             v308
brender_pix             mpeg1video              v408
c93                     mpeg2_cuvid             v410
cavs                    mpeg2_qsv               vb
cbd2_dpcm               mpeg2video              vble
ccaption                mpeg4                   vbn
cdgraphics              mpeg4_cuvid             vc1
cdtoons                 mpegvideo               vc1_cuvid
cdxl                    mpl2                    vc1_qsv
cfhd                    msa1                    vc1image
cinepak                 mscc                    vcr1
clearvideo              msmpeg4v1               vmdaudio
cljr                    msmpeg4v2               vmdvideo
cllc                    msmpeg4v3               vmix
comfortnoise            msnsiren                vmnc
cook                    msp2                    vnull
cpia                    msrle                   vorbis
cri                     mss1                    vp3
cscd                    mss2                    vp4
cyuv                    msvideo1                vp5
dca                     mszh                    vp6
dds                     mts2                    vp6a
derf_dpcm               mv30                    vp6f
dfa                     mvc1                    vp7
dfpwm                   mvc2                    vp8
dirac                   mvdv                    vp8_cuvid
dnxhd                   mvha                    vp8_qsv
dolby_e                 mwsc                    vp9
dpx                     mxpeg                   vp9_cuvid
dsd_lsbf                nellymoser              vp9_qsv
dsd_lsbf_planar         notchlc                 vplayer
dsd_msbf                nuv                     vqa
dsd_msbf_planar         on2avc                  vqc
dsicinaudio             opus                    vvc
dsicinvideo             osq                     vvc_qsv
dss_sp                  paf_audio               wady_dpcm
dst                     paf_video               wavarc
dvaudio                 pam                     wavpack
dvbsub                  pbm                     wbmp
dvdsub                  pcm_alaw                wcmv
dvvideo                 pcm_bluray              webp
dxa                     pcm_dvd                 webvtt
dxtory                  pcm_f16le               wmalossless
dxv                     pcm_f24le               wmapro
eac3                    pcm_f32be               wmav1
eacmv                   pcm_f32le               wmav2
eamad                   pcm_f64be               wmavoice
eatgq                   pcm_f64le               wmv1
eatgv                   pcm_lxf                 wmv2
eatqi                   pcm_mulaw               wmv3
eightbps                pcm_s16be               wmv3image
eightsvx_exp            pcm_s16be_planar        wnv1
eightsvx_fib            pcm_s16le               wrapped_avframe
escape124               pcm_s16le_planar        ws_snd1
escape130               pcm_s24be               xan_dpcm
evrc                    pcm_s24daud             xan_wc3
exr                     pcm_s24le               xan_wc4
fastaudio               pcm_s24le_planar        xbin
ffv1                    pcm_s32be               xbm
ffvhuff                 pcm_s32le               xface
ffwavesynth             pcm_s32le_planar        xl
fic                     pcm_s64be               xma1
fits                    pcm_s64le               xma2
flac                    pcm_s8                  xpm
flashsv                 pcm_s8_planar           xsub
flashsv2                pcm_sga                 xwd
flic                    pcm_u16be               y41p
flv                     pcm_u16le               ylc
fmvc                    pcm_u24be               yop
fourxm                  pcm_u24le               yuv4
fraps                   pcm_u32be               zero12v
frwu                    pcm_u32le               zerocodec
ftr                     pcm_u8                  zlib
g2m                     pcm_vidc                zmbv

Enabled encoders:
a64multi                hevc_nvenc              pcm_s64be
a64multi5               hevc_qsv                pcm_s64le
aac                     hevc_vaapi              pcm_s8
aac_mf                  hevc_vulkan             pcm_s8_planar
ac3                     huffyuv                 pcm_u16be
ac3_fixed               jpeg2000                pcm_u16le
ac3_mf                  jpegls                  pcm_u24be
adpcm_adx               libaom_av1              pcm_u24le
adpcm_argo              libcodec2               pcm_u32be
adpcm_g722              libgsm                  pcm_u32le
adpcm_g726              libgsm_ms               pcm_u8
adpcm_g726le            libilbc                 pcm_vidc
adpcm_ima_alp           libjxl                  pcx
adpcm_ima_amv           liblc3                  pfm
adpcm_ima_apm           libmp3lame              pgm
adpcm_ima_qt            libopencore_amrnb       pgmyuv
adpcm_ima_ssi           libopenjpeg             phm
adpcm_ima_wav           libopus                 png
adpcm_ima_ws            librav1e                ppm
adpcm_ms                libshine                prores
adpcm_swf               libspeex                prores_aw
adpcm_yamaha            libsvtav1               prores_ks
alac                    libtheora               qoi
alias_pix               libtwolame              qtrle
amv                     libvo_amrwbenc          r10k
anull                   libvorbis               r210
apng                    libvpx_vp8              ra_144
aptx                    libvpx_vp9              rawvideo
aptx_hd                 libvvenc                roq
ass                     libwebp                 roq_dpcm
asv1                    libwebp_anim            rpza
asv2                    libx264                 rv10
av1_amf                 libx264rgb              rv20
av1_mf                  libx265                 s302m
av1_nvenc               libxavs2                sbc
av1_qsv                 libxeve                 sgi
av1_vaapi               libxvid                 smc
avrp                    ljpeg                   snow
avui                    magicyuv                speedhq
bitpacked               mjpeg                   srt
bmp                     mjpeg_qsv               ssa
cfhd                    mjpeg_vaapi             subrip
cinepak                 mlp                     sunrast
cljr                    movtext                 svq1
comfortnoise            mp2                     targa
dca                     mp2fixed                text
dfpwm                   mp3_mf                  tiff
dnxhd                   mpeg1video              truehd
dpx                     mpeg2_qsv               tta
dvbsub                  mpeg2_vaapi             ttml
dvdsub                  mpeg2video              utvideo
dvvideo                 mpeg4                   v210
dxv                     msmpeg4v2               v308
eac3                    msmpeg4v3               v408
exr                     msrle                   v410
ffv1                    msvideo1                vbn
ffv1_vulkan             nellymoser              vc2
ffvhuff                 opus                    vnull
fits                    pam                     vorbis
flac                    pbm                     vp8_vaapi
flashsv                 pcm_alaw                vp9_qsv
flashsv2                pcm_bluray              vp9_vaapi
flv                     pcm_dvd                 wavpack
g723_1                  pcm_f32be               wbmp
gif                     pcm_f32le               webvtt
h261                    pcm_f64be               wmav1
h263                    pcm_f64le               wmav2
h263p                   pcm_mulaw               wmv1
h264_amf                pcm_s16be               wmv2
h264_mf                 pcm_s16be_planar        wrapped_avframe
h264_nvenc              pcm_s16le               xbm
h264_qsv                pcm_s16le_planar        xface
h264_vaapi              pcm_s24be               xsub
h264_vulkan             pcm_s24daud             xwd
hap                     pcm_s24le               y41p
hdr                     pcm_s24le_planar        yuv4
hevc_amf                pcm_s32be               zlib
hevc_d3d12va            pcm_s32le               zmbv
hevc_mf                 pcm_s32le_planar

Enabled hwaccels:
av1_d3d11va             hevc_dxva2              vc1_dxva2
av1_d3d11va2            hevc_nvdec              vc1_nvdec
av1_d3d12va             hevc_vaapi              vc1_vaapi
av1_dxva2               hevc_vulkan             vp8_nvdec
av1_nvdec               mjpeg_nvdec             vp8_vaapi
av1_vaapi               mjpeg_vaapi             vp9_d3d11va
av1_vulkan              mpeg1_nvdec             vp9_d3d11va2
h263_vaapi              mpeg2_d3d11va           vp9_d3d12va
h264_d3d11va            mpeg2_d3d11va2          vp9_dxva2
h264_d3d11va2           mpeg2_d3d12va           vp9_nvdec
h264_d3d12va            mpeg2_dxva2             vp9_vaapi
h264_dxva2              mpeg2_nvdec             vvc_vaapi
h264_nvdec              mpeg2_vaapi             wmv3_d3d11va
h264_vaapi              mpeg4_nvdec             wmv3_d3d11va2
h264_vulkan             mpeg4_vaapi             wmv3_d3d12va
hevc_d3d11va            vc1_d3d11va             wmv3_dxva2
hevc_d3d11va2           vc1_d3d11va2            wmv3_nvdec
hevc_d3d12va            vc1_d3d12va             wmv3_vaapi

Enabled parsers:
aac                     dvdsub                  mpegvideo
aac_latm                evc                     opus
ac3                     flac                    png
adx                     ftr                     pnm
amr                     g723_1                  qoi
av1                     g729                    rv34
avs2                    gif                     sbc
avs3                    gsm                     sipr
bmp                     h261                    tak
cavsvideo               h263                    vc1
cook                    h264                    vorbis
cri                     hdr                     vp3
dca                     hevc                    vp8
dirac                   ipu                     vp9
dnxhd                   jpeg2000                vvc
dnxuc                   jpegxl                  webp
dolby_e                 misc4                   xbm
dpx                     mjpeg                   xma
dvaudio                 mlp                     xwd
dvbsub                  mpeg4video
dvd_nav                 mpegaudio

Enabled demuxers:
aa                      idf                     pcm_f64le
aac                     iff                     pcm_mulaw
aax                     ifv                     pcm_s16be
ac3                     ilbc                    pcm_s16le
ac4                     image2                  pcm_s24be
ace                     image2_alias_pix        pcm_s24le
acm                     image2_brender_pix      pcm_s32be
act                     image2pipe              pcm_s32le
adf                     image_bmp_pipe          pcm_s8
adp                     image_cri_pipe          pcm_u16be
ads                     image_dds_pipe          pcm_u16le
adx                     image_dpx_pipe          pcm_u24be
aea                     image_exr_pipe          pcm_u24le
afc                     image_gem_pipe          pcm_u32be
aiff                    image_gif_pipe          pcm_u32le
aix                     image_hdr_pipe          pcm_u8
alp                     image_j2k_pipe          pcm_vidc
amr                     image_jpeg_pipe         pdv
amrnb                   image_jpegls_pipe       pjs
amrwb                   image_jpegxl_pipe       pmp
anm                     image_pam_pipe          pp_bnk
apac                    image_pbm_pipe          pva
apc                     image_pcx_pipe          pvf
ape                     image_pfm_pipe          qcp
apm                     image_pgm_pipe          qoa
apng                    image_pgmyuv_pipe       r3d
aptx                    image_pgx_pipe          rawvideo
aptx_hd                 image_phm_pipe          rcwt
aqtitle                 image_photocd_pipe      realtext
argo_asf                image_pictor_pipe       redspark
argo_brp                image_png_pipe          rka
argo_cvg                image_ppm_pipe          rl2
asf                     image_psd_pipe          rm
asf_o                   image_qdraw_pipe        roq
ass                     image_qoi_pipe          rpl
ast                     image_sgi_pipe          rsd
au                      image_sunrast_pipe      rso
av1                     image_svg_pipe          rtp
avi                     image_tiff_pipe         rtsp
avisynth                image_vbn_pipe          s337m
avr                     image_webp_pipe         sami
avs                     image_xbm_pipe          sap
avs2                    image_xpm_pipe          sbc
avs3                    image_xwd_pipe          sbg
bethsoftvid             imf                     scc
bfi                     ingenient               scd
bfstm                   ipmovie                 sdns
bink                    ipu                     sdp
binka                   ircam                   sdr2
bintext                 iss                     sds
bit                     iv8                     sdx
bitpacked               ivf                     segafilm
bmv                     ivr                     ser
boa                     jacosub                 sga
bonk                    jpegxl_anim             shorten
brstm                   jv                      siff
c93                     kux                     simbiosis_imx
caf                     kvag                    sln
cavsvideo               laf                     smacker
cdg                     lc3                     smjpeg
cdxl                    libgme                  smush
cine                    libmodplug              sol
codec2                  libopenmpt              sox
codec2raw               live_flv                spdif
concat                  lmlm4                   srt
dash                    loas                    stl
data                    lrc                     str
daud                    luodat                  subviewer
dcstr                   lvf                     subviewer1
derf                    lxf                     sup
dfa                     m4v                     svag
dfpwm                   matroska                svs
dhav                    mca                     swf
dirac                   mcc                     tak
dnxhd                   mgsts                   tedcaptions
dsf                     microdvd                thp
dsicin                  mjpeg                   threedostr
dss                     mjpeg_2000              tiertexseq
dts                     mlp                     tmv
dtshd                   mlv                     truehd
dv                      mm                      tta
dvbsub                  mmf                     tty
dvbtxt                  mods                    txd
dxa                     moflex                  ty
ea                      mov                     usm
ea_cdata                mp3                     v210
eac3                    mpc                     v210x
epaf                    mpc8                    vag
evc                     mpegps                  vc1
ffmetadata              mpegts                  vc1t
filmstrip               mpegtsraw               vividas
fits                    mpegvideo               vivo
flac                    mpjpeg                  vmd
flic                    mpl2                    vobsub
flv                     mpsub                   voc
fourxm                  msf                     vpk
frm                     msnwc_tcp               vplayer
fsb                     msp                     vqf
fwse                    mtaf                    vvc
g722                    mtv                     w64
g723_1                  musx                    wady
g726                    mv                      wav
g726le                  mvi                     wavarc
g729                    mxf                     wc3
gdv                     mxg                     webm_dash_manifest
genh                    nc                      webvtt
gif                     nistsphere              wsaud
gsm                     nsp                     wsd
gxf                     nsv                     wsvqa
h261                    nut                     wtv
h263                    nuv                     wv
h264                    obu                     wve
hca                     ogg                     xa
hcom                    oma                     xbin
hevc                    osq                     xmd
hls                     paf                     xmv
hnm                     pcm_alaw                xvag
iamf                    pcm_f32be               xwma
ico                     pcm_f32le               yop
idcin                   pcm_f64be               yuv4mpegpipe

Enabled muxers:
a64                     h263                    pcm_s24be
ac3                     h264                    pcm_s24le
ac4                     hash                    pcm_s32be
adts                    hds                     pcm_s32le
adx                     hevc                    pcm_s8
aea                     hls                     pcm_u16be
aiff                    iamf                    pcm_u16le
alp                     ico                     pcm_u24be
amr                     ilbc                    pcm_u24le
amv                     image2                  pcm_u32be
apm                     image2pipe              pcm_u32le
apng                    ipod                    pcm_u8
aptx                    ircam                   pcm_vidc
aptx_hd                 ismv                    psp
argo_asf                ivf                     rawvideo
argo_cvg                jacosub                 rcwt
asf                     kvag                    rm
asf_stream              latm                    roq
ass                     lc3                     rso
ast                     lrc                     rtp
au                      m4v                     rtp_mpegts
avi                     matroska                rtsp
avif                    matroska_audio          sap
avm2                    md5                     sbc
avs2                    microdvd                scc
avs3                    mjpeg                   segafilm
bit                     mkvtimestamp_v2         segment
caf                     mlp                     smjpeg
cavsvideo               mmf                     smoothstreaming
chromaprint             mov                     sox
codec2                  mp2                     spdif
codec2raw               mp3                     spx
crc                     mp4                     srt
dash                    mpeg1system             stream_segment
data                    mpeg1vcd                streamhash
daud                    mpeg1video              sup
dfpwm                   mpeg2dvd                swf
dirac                   mpeg2svcd               tee
dnxhd                   mpeg2video              tg2
dts                     mpeg2vob                tgp
dv                      mpegts                  truehd
eac3                    mpjpeg                  tta
evc                     mxf                     ttml
f4v                     mxf_d10                 uncodedframecrc
ffmetadata              mxf_opatom              vc1
fifo                    null                    vc1t
filmstrip               nut                     voc
fits                    obu                     vvc
flac                    oga                     w64
flv                     ogg                     wav
framecrc                ogv                     webm
framehash               oma                     webm_chunk
framemd5                opus                    webm_dash_manifest
g722                    pcm_alaw                webp
g723_1                  pcm_f32be               webvtt
g726                    pcm_f32le               wsaud
g726le                  pcm_f64be               wtv
gif                     pcm_f64le               wv
gsm                     pcm_mulaw               yuv4mpegpipe
gxf                     pcm_s16be
h261                    pcm_s16le

Enabled protocols:
async                   http                    rtmp
bluray                  httpproxy               rtmpe
cache                   https                   rtmps
concat                  icecast                 rtmpt
concatf                 ipfs_gateway            rtmpte
crypto                  ipns_gateway            rtmpts
data                    librist                 rtp
fd                      libsrt                  srtp
ffrtmpcrypt             libssh                  subfile
ffrtmphttp              libzmq                  tcp
file                    md5                     tee
ftp                     mmsh                    tls
gopher                  mmst                    udp
gophers                 pipe                    udplite
hls                     prompeg

Enabled filters:
a3dscope                ddagrab                 pan
aap                     deband                  perlin
abench                  deblock                 perms
abitscope               decimate                perspective
acompressor             deconvolve              phase
acontrast               dedot                   photosensitivity
acopy                   deesser                 pixdesctest
acrossfade              deflate                 pixelize
acrossover              deflicker               pixscope
acrusher                deinterlace_qsv         pp
acue                    deinterlace_vaapi       pp7
addroi                  dejudder                premultiply
adeclick                delogo                  prewitt
adeclip                 denoise_vaapi           prewitt_opencl
adecorrelate            deshake                 procamp_vaapi
adelay                  deshake_opencl          program_opencl
adenorm                 despill                 pseudocolor
aderivative             detelecine              psnr
adrawgraph              dialoguenhance          pullup
adrc                    dilation                qp
adynamicequalizer       dilation_opencl         qrencode
adynamicsmooth          displace                qrencodesrc
aecho                   doubleweave             quirc
aemphasis               drawbox                 random
aeval                   drawbox_vaapi           readeia608
aevalsrc                drawgraph               readvitc
aexciter                drawgrid                realtime
afade                   drawtext                remap
afdelaysrc              drmeter                 remap_opencl
afftdn                  dynaudnorm              removegrain
afftfilt                earwax                  removelogo
afir                    ebur128                 repeatfields
afireqsrc               edgedetect              replaygain
afirsrc                 elbg                    reverse
aformat                 entropy                 rgbashift
afreqshift              epx                     rgbtestsrc
afwtdn                  eq                      roberts
agate                   equalizer               roberts_opencl
agraphmonitor           erosion                 rotate
ahistogram              erosion_opencl          rubberband
aiir                    estdif                  sab
aintegral               exposure                scale
ainterleave             extractplanes           scale2ref
alatency                extrastereo             scale_cuda
alimiter                fade                    scale_qsv
allpass                 feedback                scale_vaapi
allrgb                  fftdnoiz                scale_vulkan
allyuv                  fftfilt                 scdet
aloop                   field                   scharr
alphaextract            fieldhint               scroll
alphamerge              fieldmatch              segment
amerge                  fieldorder              select
ametadata               fillborders             selectivecolor
amix                    find_rect               sendcmd
amovie                  firequalizer            separatefields
amplify                 flanger                 setdar
amultiply               flip_vulkan             setfield
anequalizer             flite                   setparams
anlmdn                  floodfill               setpts
anlmf                   format                  setrange
anlms                   fps                     setsar
anoisesrc               framepack               settb
anull                   framerate               sharpness_vaapi
anullsink               framestep               shear
anullsrc                freezedetect            showcqt
apad                    freezeframes            showcwt
aperms                  frei0r                  showfreqs
aphasemeter             frei0r_src              showinfo
aphaser                 fspp                    showpalette
aphaseshift             fsync                   showspatial
apsnr                   gblur                   showspectrum
apsyclip                gblur_vulkan            showspectrumpic
apulsator               geq                     showvolume
arealtime               gradfun                 showwaves
aresample               gradients               showwavespic
areverse                graphmonitor            shuffleframes
arls                    grayworld               shufflepixels
arnndn                  greyedge                shuffleplanes
asdr                    guided                  sidechaincompress
asegment                haas                    sidechaingate
aselect                 haldclut                sidedata
asendcmd                haldclutsrc             sierpinski
asetnsamples            hdcd                    signalstats
asetpts                 headphone               signature
asetrate                hflip                   silencedetect
asettb                  hflip_vulkan            silenceremove
ashowinfo               highpass                sinc
asidedata               highshelf               sine
asisdr                  hilbert                 siti
asoftclip               histeq                  smartblur
aspectralstats          histogram               smptebars
asplit                  hqdn3d                  smptehdbars
ass                     hqx                     sobel
astats                  hstack                  sobel_opencl
astreamselect           hstack_qsv              sofalizer
asubboost               hstack_vaapi            spectrumsynth
asubcut                 hsvhold                 speechnorm
asupercut               hsvkey                  split
asuperpass              hue                     spp
asuperstop              huesaturation           ssim
atadenoise              hwdownload              ssim360
atempo                  hwmap                   stereo3d
atilt                   hwupload                stereotools
atrim                   hwupload_cuda           stereowiden
avectorscope            hysteresis              streamselect
avgblur                 identity                subtitles
avgblur_opencl          idet                    super2xsai
avgblur_vulkan          il                      superequalizer
avsynctest              inflate                 surround
axcorrelate             interlace               swaprect
azmq                    interleave              swapuv
backgroundkey           join                    tblend
bandpass                kerndeint               telecine
bandreject              kirsch                  testsrc
bass                    ladspa                  testsrc2
bbox                    lagfun                  thistogram
bench                   latency                 threshold
bilateral               lenscorrection          thumbnail
bilateral_cuda          lensfun                 thumbnail_cuda
biquad                  libplacebo              tile
bitplanenoise           libvmaf                 tiltandshift
blackdetect             life                    tiltshelf
blackframe              limitdiff               tinterlace
blend                   limiter                 tlut2
blend_vulkan            loop                    tmedian
blockdetect             loudnorm                tmidequalizer
blurdetect              lowpass                 tmix
bm3d                    lowshelf                tonemap
boxblur                 lumakey                 tonemap_opencl
boxblur_opencl          lut                     tonemap_vaapi
bs2b                    lut1d                   tpad
bwdif                   lut2                    transpose
bwdif_cuda              lut3d                   transpose_opencl
bwdif_vulkan            lutrgb                  transpose_vaapi
cas                     lutyuv                  transpose_vulkan
ccrepack                mandelbrot              treble
cellauto                maskedclamp             tremolo
channelmap              maskedmax               trim
channelsplit            maskedmerge             unpremultiply
chorus                  maskedmin               unsharp
chromaber_vulkan        maskedthreshold         unsharp_opencl
chromahold              maskfun                 untile
chromakey               mcdeint                 uspp
chromakey_cuda          mcompand                v360
chromanr                median                  vaguedenoiser
chromashift             mergeplanes             varblur
ciescope                mestimate               vectorscope
codecview               metadata                vflip
color                   midequalizer            vflip_vulkan
color_vulkan            minterpolate            vfrdet
colorbalance            mix                     vibrance
colorchannelmixer       monochrome              vibrato
colorchart              morpho                  vidstabdetect
colorcontrast           movie                   vidstabtransform
colorcorrect            mpdecimate              vif
colorhold               mptestsrc               vignette
colorize                msad                    virtualbass
colorkey                multiply                vmafmotion
colorkey_opencl         negate                  volume
colorlevels             nlmeans                 volumedetect
colormap                nlmeans_opencl          vpp_qsv
colormatrix             nlmeans_vulkan          vstack
colorspace              nnedi                   vstack_qsv
colorspace_cuda         noformat                vstack_vaapi
colorspectrum           noise                   w3fdif
colortemperature        normalize               waveform
compand                 null                    weave
compensationdelay       nullsink                xbr
concat                  nullsrc                 xcorrelate
convolution             openclsrc               xfade
convolution_opencl      oscilloscope            xfade_opencl
convolve                overlay                 xfade_vulkan
copy                    overlay_cuda            xmedian
corr                    overlay_opencl          xpsnr
cover_rect              overlay_qsv             xstack
crop                    overlay_vaapi           xstack_qsv
cropdetect              overlay_vulkan          xstack_vaapi
crossfeed               owdenoise               yadif
crystalizer             pad                     yadif_cuda
cue                     pad_opencl              yaepblur
curves                  pad_vaapi               yuvtestsrc
datascope               pal100bars              zmq
dblur                   pal75bars               zoneplate
dcshift                 palettegen              zoompan
dctdnoiz                paletteuse              zscale

Enabled bsfs:
aac_adtstoasc           h264_mp4toannexb        pcm_rechunk
av1_frame_merge         h264_redundant_pps      pgs_frame_merge
av1_frame_split         hapqa_extract           prores_metadata
av1_metadata            hevc_metadata           remove_extradata
chomp                   hevc_mp4toannexb        setts
dca_core                imx_dump_header         showinfo
dovi_rpu                media100_to_mjpegb      text2movsub
dts2pts                 mjpeg2jpeg              trace_headers
dump_extradata          mjpega_dump_header      truehd_core
dv_error_marker         mov2textsub             vp9_metadata
eac3_core               mpeg2_metadata          vp9_raw_reorder
evc_frame_merge         mpeg4_unpack_bframes    vp9_superframe
extract_extradata       noise                   vp9_superframe_split
filter_units            null                    vvc_metadata
h264_metadata           opus_metadata           vvc_mp4toannexb

Enabled indevs:
dshow                   lavfi                   vfwcap
gdigrab                 libcdio

Enabled outdevs:
caca                    sdl2

git-full external libraries' versions: 

AMF v1.4.35-3-g8f5a645
aom v3.11.0-110-g37c5c4e6aa
aribb24 v1.0.3-5-g5e9be27
aribcaption 1.1.1
AviSynthPlus v3.7.3-80-g452cea05
bs2b 3.1.0
chromaprint 1.5.1
codec2 1.2.0-103-gff00a6e2
dav1d 1.5.0-42-gf8d2620
davs2 1.7-1-gb41cf11
ffnvcodec n12.2.72.0-1-g9934f17
flite v2.2-55-g6c9f20d
freetype VER-2-13-3
frei0r v2.3.3-7-g9178c72
fribidi v1.0.16
gsm 1.0.22
harfbuzz 10.1.0-17-g0b7beefd
ladspa-sdk 1.17
lame 3.100
lc3 1.1.0
lensfun v0.3.95-1587-g3a69a2e8
libass 0.17.3-38-g159cefc
libcdio-paranoia 10.2
libgme 0.6.3
libilbc v3.0.4-346-g6adb26d4a4
libopencore-amrnb 0.1.6
libopencore-amrwb 0.1.6
libplacebo v7.349.0-26-g5788a82
libsoxr 0.1.3
libssh 0.11.1
libtheora 1.1.1
libwebp webp-rfc9649-8-g4c85d860
oneVPL 2.13
OpenCL-Headers v2024.10.24
openmpt libopenmpt-0.6.20-19-gc8153cd77
opus v1.5.2-22-g7db26934
qrencode 4.1.1
quirc 1.2
rav1e p20241015
rist 0.2.11
rubberband v1.8.1
SDL prerelease-2.29.2-432-gba433e4a5
shaderc v2024.3-5-g8c4d729
shine 3.1.1
snappy 1.2.1
speex Speex-1.2.1-29-gaca6801
srt v1.5.4-5-g5f16494
SVT-AV1 v2.3.0-58-gc642bb04
twolame 0.4.0
uavs3d v1.1-47-g1fd0491
VAAPI 2.23.0.
vidstab v1.1.1-13-g8dff7ad
vmaf v3.0.0-99-g8cde19dc
vo-amrwbenc 0.1.3
vorbis v1.3.7-10-g84c02369
vpx v1.15.0-28-g6f0c446c7
vulkan-loader v1.3.302
vvenc v1.12.0-40-g7cf1e5f
x264 v0.164.3198
x265 4.1-54-gfa2770934
xavs2 1.4
xevd 0.5.0
xeve 0.5.1
xvid v1.3.7
zeromq 4.3.5
zimg release-3.0.5-173-g30f368c
zvbi v0.2.42-58-ga48ab3a

