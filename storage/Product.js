const Product = require("../models/Product");

const products = [
    {
    _id: "65a7e45902e12c44f599444e",
    title: "E - STUD BIG HEART GEM AND SINGLE GEM",
    description: "---",
    price: 240000,
    discountPercentage: 12.96,
    stockQuantity: 14,
    brand: "65a7e20102e12c44f59943db",
    category: "65a7e24602e12c44f599442c",
    thumbnail: "/images/E/E - STUD BIG HEART GEM AND SINGLE GEM/IMG_7969.PNG",
    images: [
      "/images/E/E - STUD BIG HEART GEM AND SINGLE GEM/IMG_7969.PNG",
      "/images/E/E - STUD BIG HEART GEM AND SINGLE GEM/IMG_7970.PNG",
      "/images/E/E - STUD BIG HEART GEM AND SINGLE GEM/IMG_7971.PNG",
      "/images/E/E - STUD BIG HEART GEM AND SINGLE GEM/IMG_7972.PNG",
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994450",
    title: "E - STUD BOW MULTI GEM",
    description:
      "---",
    price: 210000,
    discountPercentage: 15.46,
    stockQuantity: 36,
    brand: "65a7e20102e12c44f59943db",
    category: "65a7e24602e12c44f599442c",
    thumbnail: "/images/E/E - STUD BOW MULTI GEM/IMG_7973.PNG",
    images: ["/images/E/E - STUD BOW MULTI GEM/IMG_7973.PNG",
      "/images/E/E - STUD BOW MULTI GEM/IMG_7974.PNG",
      "/images/E/E - STUD BOW MULTI GEM/IMG_7975.PNG",
      "/images/E/E - STUD BOW MULTI GEM/IMG_7977.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994451",
    title: "E - STUD CIRCLE GEM WITH BUTTERFLY",
    description: "---",
    price: 200000,
    discountPercentage: 450000,
    stockQuantity: 123,
    brand: "65a7e20102e12c44f59943db",
    category: "65a7e24602e12c44f599442c",
    thumbnail: "/images/E/E - STUD CIRCLE GEM WITH BUTTERFLY/IMG_7984.PNG",
    images: [
      "/images/E/E - STUD CIRCLE GEM WITH BUTTERFLY/IMG_7984.PNG",
      "/images/E/E - STUD CIRCLE GEM WITH BUTTERFLY/IMG_7985.PNG",
      "/images/E/E - STUD CIRCLE GEM WITH BUTTERFLY/IMG_7986.PNG",
      "/images/E/E - STUD CIRCLE GEM WITH BUTTERFLY/IMG_7987.PNG",
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994452",
    title: "E - STUD SPECIAL CLOVER GEM",
    description:
      "---",
    price: 240000,
    discountPercentage: 10.58,
    stockQuantity: 32,
    brand: "65a7e20102e12c44f59943db",
    category: "65a7e24602e12c44f599442c",
    thumbnail: "/images/E/E - STUD SPECIAL CLOVER GEM/IMG_7988.PNG",
    images: [
      "/images/E/E - STUD SPECIAL CLOVER GEM/IMG_7988.PNG",
      "/images/E/E - STUD SPECIAL CLOVER GEM/IMG_7989.PNG",
      "/images/E/E - STUD SPECIAL CLOVER GEM/IMG_7990.PNG",
      "/images/E/E - STUD SPECIAL CLOVER GEM/IMG_7991.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994453",
    title: "B - MIX LULTI PEARL AND DROP CHARM",
    description:
      "---",
    price: 330000,
    discountPercentage: 11.02,
    stockQuantity: 83,
    brand: "65a7e20102e12c44f59943dc",
    category: "65a7e24602e12c44f599442d",
    thumbnail: "/images/B/B - MIX LULTI PEARL AND DROP CHARM/IMG_7968.PNG",
    images: [
      "/images/B/B - MIX LULTI PEARL AND DROP CHARM/IMG_7968.PNG",
      "/images/B/B - MIX LULTI PEARL AND DROP CHARM/IMG_7965.PNG",
      "/images/B/B - MIX LULTI PEARL AND DROP CHARM/IMG_7966.PNG",
      "/images/B/B - MIX LULTI PEARL AND DROP CHARM/IMG_7967.PNG",
      "/images/B/B - MIX LULTI PEARL AND DROP CHARM/IMG_7964.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994454",
    title: "B - PINK BOW GEM",
    description:
      "---",
    price: 300000,
    discountPercentage: 4.15,
    stockQuantity: 50,
    brand: "65a7e20102e12c44f59943dc",
    category: "65a7e24602e12c44f599442d",
    thumbnail: "/images/B/B - PINK BOW GEM/IMG_7930.PNG",
    images: [
      "/images/B/B - PINK BOW GEM/IMG_7930.PNG",
      "/images/B/B - PINK BOW GEM/IMG_7929.PNG",
      "/images/B/B - PINK BOW GEM/IMG_7931.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994455",
    title: "B - SPECIAL CLOVER LEAF BLINK GEM",
    description:
      "---",
    price: 320000,
    discountPercentage: 10.23,
    stockQuantity: 68,
    brand: "65a7e20102e12c44f59943dc",
    category: "65a7e24602e12c44f599442d",
    thumbnail: "/images/B/B - SPECIAL CLOVER LEAF BLINK GEM/IMG_7905.PNG",
    images: [
      "/images/B/B - SPECIAL CLOVER LEAF BLINK GEM/IMG_7905.PNG",
      "/images/B/B - SPECIAL CLOVER LEAF BLINK GEM/IMG_7906.PNG",
      "/images/B/B - SPECIAL CLOVER LEAF BLINK GEM/IMG_7907.PNG",
      "/images/B/B - SPECIAL CLOVER LEAF BLINK GEM/IMG_7908.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994456",
    title: "B - STARFISH AND SCALLOP SHELL DROP CHARM",
    description:
      "---",
    price: 280000,
    discountPercentage: 11.83,
    stockQuantity: 96,
    brand: "65a7e20102e12c44f59943dc",
    category: "65a7e24602e12c44f599442d",
    thumbnail: "/images/B/B - STARFISH AND SCALLOP SHELL DROP CHARM/IMG_7960.PNG",
    images: [
      "/images/B/B - STARFISH AND SCALLOP SHELL DROP CHARM/IMG_7960.PNG",
      "/images/B/B - STARFISH AND SCALLOP SHELL DROP CHARM/IMG_7961.PNG",
      "/images/B/B - STARFISH AND SCALLOP SHELL DROP CHARM/IMG_7962.PNG",
      "/images/B/B - STARFISH AND SCALLOP SHELL DROP CHARM/IMG_7963.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994457",
    title: "B - TRIPLE HEART PINK STONE",
    description:
      "---",
    price: 310000,
    discountPercentage: 6.18,
    stockQuantity: 89,
    brand: "65a7e20102e12c44f59943dc",
    category: "65a7e24602e12c44f599442d",
    thumbnail: "/images/B/B - TRIPLE HEART PINK STONE/IMG_7914.PNG",
    images: [
      "/images/B/B - TRIPLE HEART PINK STONE/IMG_7914.PNG",
      "/images/B/B - TRIPLE HEART PINK STONE/IMG_7911.PNG",
      "/images/B/B - TRIPLE HEART PINK STONE/IMG_7912.PNG",
      "/images/B/B - TRIPLE HEART PINK STONE/IMG_7913.PNG",
      "/images/B/B - TRIPLE HEART PINK STONE/IMG_7910.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f599445d",
    title: "N - BLING TRIPLE RINGS",
    description:
      "---",
    price: 280000,
    discountPercentage: 13.31,
    stockQuantity: 110,
    brand: "65a7e20102e12c44f59943de",
    category: "65a7e24602e12c44f599442f",
    thumbnail: "/images/N/N - BLING TRIPLE RINGS/IMG_7916.PNG",
    images: [
      "/images/N/N - BLING TRIPLE RINGS/IMG_7916.PNG",
      "/images/N/N - BLING TRIPLE RINGS/IMG_7917.PNG",
      "/images/N/N - BLING TRIPLE RINGS/IMG_7945.PNG",
      "/images/N/N - BLING TRIPLE RINGS/IMG_7946.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f599445e",
    title: "N - CIRCLE WITH MINI FLOWER GEM",
    description:
      "---",
    price: 310000,
    discountPercentage: 4.09,
    stockQuantity: 78,
    brand: "65a7e20102e12c44f59943de",
    category: "65a7e24602e12c44f599442f",
    thumbnail: "/images/N/N - CIRCLE WITH MINI FLOWER GEM/IMG_7933.PNG",
    images: [
      "/images/N/N - CIRCLE WITH MINI FLOWER GEM/IMG_7933.PNG",
      "/images/N/N - CIRCLE WITH MINI FLOWER GEM/IMG_7934.PNG",
      "/images/N/N - CIRCLE WITH MINI FLOWER GEM/IMG_7935.PNG",
      "/images/N/N - CIRCLE WITH MINI FLOWER GEM/IMG_7937.PNG",
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f599445f",
    title: "N - CUTIE PEARL HORSE GEM",
    description:
      "---",
    price: 310000,
    discountPercentage: 13.1,
    stockQuantity: 88,
    brand: "65a7e20102e12c44f59943de",
    category: "65a7e24602e12c44f599442f",
    thumbnail: "/images/N/N - CUTIE PEARL HORSE GEM/IMG_7927.PNG",
    images: [
      "/images/N/N - CUTIE PEARL HORSE GEM/IMG_7927.PNG",
      "/images/N/N - CUTIE PEARL HORSE GEM/IMG_7926.PNG",
      "/images/N/N - CUTIE PEARL HORSE GEM/IMG_7925.PNG",
      "/images/N/N - CUTIE PEARL HORSE GEM/IMG_7928.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994460",
    title: "N - MINI FLOWER AND SINGLE GEM",
    description:
      "---",
    price: 310000,
    discountPercentage: 10.68,
    stockQuantity: 54,
    brand: "65a7e20102e12c44f59943de",
    category: "65a7e24602e12c44f599442f",
    thumbnail: "/images/N/N - MINI FLOWER AND SINGLE GEM/IMG_7955.PNG",
    images: [
      "/images/N/N - MINI FLOWER AND SINGLE GEM/IMG_7955.PNG",
      "/images/N/N - MINI FLOWER AND SINGLE GEM/IMG_7954.PNG",
      "/images/N/N - MINI FLOWER AND SINGLE GEM/IMG_7953.PNG",
      "/images/N/N - MINI FLOWER AND SINGLE GEM/IMG_7956.PNG",
      "/images/N/N - MINI FLOWER AND SINGLE GEM/IMG_7957.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994461",
    title: "N - BOW AND PINK HEART",
    description:
      "---",
    price: 330000,
    discountPercentage: 16.99,
    stockQuantity: 140,
    brand: "65a7e20102e12c44f59943de",
    category: "65a7e24602e12c44f599442f",
    thumbnail: "/images/N/N - BOW AND PINK HEART/IMG_7944.PNG",
    images: [
      "/images/N/N - BOW AND PINK HEART/IMG_7944.PNG",
      "/images/N/N - BOW AND PINK HEART/IMG_7943.PNG",
      "/images/N/N - BOW AND PINK HEART/IMG_7942.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994462",
    title: "A - MULTI BALL",
    description: "---",
    price: 300000,
    discountPercentage: 4.81,
    stockQuantity: 133,
    brand: "65a7e20102e12c44f59943dd",
    category: "65a7e24602e12c44f5994430",
    thumbnail: "/images/A/A - MULTI BALL/IMG_8005.PNG",
    images: [
      "/images/A/A - MULTI BALL/IMG_8005.PNG",
      "/images/A/A - MULTI BALL/IMG_8006.PNG",
      "/images/A/A - MULTI BALL/IMG_8003.PNG",
      "/images/A/A - MULTI BALL/IMG_8004.PNG",
      "/images/A/A - MULTI BALL/IMG_8007.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994463",
    title: "A - MULTI BALL AND DROP BELL",
    description: "---",
    price: 310000,
    discountPercentage: 15.58,
    stockQuantity: 146,
    brand: "65a7e20102e12c44f59943dd",
    category: "65a7e24602e12c44f5994430",
    thumbnail: "/images/A/A - MULTI BALL AND DROP BELL/IMG_8009.PNG",
    images: [
      "/images/A/A - MULTI BALL AND DROP BELL/IMG_8009.PNG",
      "/images/A/A - MULTI BALL AND DROP BELL/IMG_8008.PNG",
      "/images/A/A - MULTI BALL AND DROP BELL/IMG_8010.PNG",
      "/images/A/A - MULTI BALL AND DROP BELL/IMG_8011.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994464",
    title: "A - MULTI BALL DOUBLE LINE",
    description:
      "---",
    price: 340000,
    discountPercentage: 8.04,
    stockQuantity: 26,
    brand: "65a7e20102e12c44f59943dd",
    category: "65a7e24602e12c44f5994430",
    thumbnail: "/images/A/A - MULTI BALL DOUBLE LINE/IMG_8014.PNG",
    images: [
      "/images/A/A - MULTI BALL DOUBLE LINE/IMG_8014.PNG",
      "/images/A/A - MULTI BALL DOUBLE LINE/IMG_8013.PNG",
      "/images/A/A - MULTI BALL DOUBLE LINE/IMG_8012.PNG",
      "/images/A/A - MULTI BALL DOUBLE LINE/IMG_8015.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f5994469",
    title: "R - MIDI FLOWER DOUBLE LEAF GEM",
    description:
      "---",
    price: 380000,
    discountPercentage: 16.49,
    stockQuantity: 54,
    brand: "65a7e20102e12c44f59943da",
    category: "65a7e24602e12c44f5994431",
    thumbnail: "/images/R/R - MIDI FLOWER DOUBLE LEAF GEM/IMG_7983.PNG",
    images: [
      "/images/R/R - MIDI FLOWER DOUBLE LEAF GEM/IMG_7983.PNG",
      "/images/R/R - MIDI FLOWER DOUBLE LEAF GEM/IMG_7982.PNG",
      "/images/R/R - MIDI FLOWER DOUBLE LEAF GEM/IMG_7981.PNG",
      "/images/R/R - MIDI FLOWER DOUBLE LEAF GEM/IMG_7980.PNG",
      "/images/R/R - MIDI FLOWER DOUBLE LEAF GEM/IMG_7979.PNG",
      "/images/R/R - MIDI FLOWER DOUBLE LEAF GEM/IMG_7978.PNG",
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f599446a",
    title: "R - MIDI PRINCESS CIRCLE GEM",
    description:
      "---",
    price: 430000,
    discountPercentage: 15.34,
    stockQuantity: 7,
    brand: "65a7e20102e12c44f59943da",
    category: "65a7e24602e12c44f5994431",
    thumbnail: "/images/R/R - MIDI PRINCESS CIRCLE GEM/IMG_7997.PNG",
    images: [
      "/images/R/R - MIDI PRINCESS CIRCLE GEM/IMG_7997.PNG",
      "/images/R/R - MIDI PRINCESS CIRCLE GEM/IMG_7998.PNG",
      "/images/R/R - MIDI PRINCESS CIRCLE GEM/IMG_7999.PNG",
      "/images/R/R - MIDI PRINCESS CIRCLE GEM/IMG_8001.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
  {
    _id: "65a7e45902e12c44f599446b",
    title: "R - MIDI SLAY BUTTERFLY CRYSTAL STONE AND MULTI GEM",
    description:
      "---",
    price: 380000,
    discountPercentage: 2.92,
    stockQuantity: 54,
    brand: "65a7e20102e12c44f59943da",
    category: "65a7e24602e12c44f5994431",
    thumbnail: "/images/R/R - MIDI SLAY BUTTERFLY CRYSTAL STONE AND MULTI GEM/IMG_7992.PNG",
    images: [
      "/images/R/R - MIDI SLAY BUTTERFLY CRYSTAL STONE AND MULTI GEM/IMG_7992.PNG",
      "/images/R/R - MIDI SLAY BUTTERFLY CRYSTAL STONE AND MULTI GEM/IMG_7993.PNG",
      "/images/R/R - MIDI SLAY BUTTERFLY CRYSTAL STONE AND MULTI GEM/IMG_7994.PNG",
      "/images/R/R - MIDI SLAY BUTTERFLY CRYSTAL STONE AND MULTI GEM/IMG_7995.PNG",
      "/images/R/R - MIDI SLAY BUTTERFLY CRYSTAL STONE AND MULTI GEM/IMG_7996.PNG"
    ],
    isDeleted: false,
    updatedAt: "2024-02-07T09:22:57.840Z",
  },
];

exports.seedProduct = async () => {
  try {
    await Product.deleteMany({});
    await Product.insertMany(products);
    console.log("Product seeded successfully");
  } catch (error) {
    console.log(error);
  }
};