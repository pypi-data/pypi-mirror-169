/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.5.1"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* First part of user prologue.  */
#line 4 "src/grammar/dice.yacc"


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <limits.h>
#include "yacc_header.h"
#include "vector_functions.h"
#include "shared_header.h"
#include "dice_logic.h"
#include "macro_logic.h"
#include "rolls/sided_dice.h"
#include "rolls/condition_checking.h"

#define UNUSED(x) (void)(x)

int yylex(void);
int yyerror(const char* s);
void print_err_if_present(int err_code);

int yydebug=1;
int verbose = 1;
int seeded = 0;
int write_to_file = 0;
char * output_file;

// Registers

// TODO: It would be better to fit arbitrary length strings.
unsigned int MAX_SYMBOL_TEXT_LENGTH = 100;
unsigned int MAX_ITERATION = 20;

int initialize(){
    if (!seeded){
        srand(time(0));
        seeded = 1;
    }
    return 0;
}

int collapse(int * arr, int len){
    return sum(arr, len);
}

int sum(int * arr, int len){
    int result = 0;
    for(int i = 0; i != len; i++) result += arr[i];
    return result;
}

int roll_numeric_die(int small, int big){
    return random_fn(small, big);
}
int roll_symbolic_die(int length_of_symbolic_array){
    // Returns random index into symbolic array
    return roll_numeric_die(0, length_of_symbolic_array -1);
}



#line 132 "y.tab.c"

# ifndef YY_CAST
#  ifdef __cplusplus
#   define YY_CAST(Type, Val) static_cast<Type> (Val)
#   define YY_REINTERPRET_CAST(Type, Val) reinterpret_cast<Type> (Val)
#  else
#   define YY_CAST(Type, Val) ((Type) (Val))
#   define YY_REINTERPRET_CAST(Type, Val) ((Type) (Val))
#  endif
# endif
# ifndef YY_NULLPTR
#  if defined __cplusplus
#   if 201103L <= __cplusplus
#    define YY_NULLPTR nullptr
#   else
#    define YY_NULLPTR 0
#   endif
#  else
#   define YY_NULLPTR ((void*)0)
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* Use api.header.include to #include this header
   instead of duplicating it here.  */
#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    NUMBER = 258,
    SIDED_DIE = 259,
    FATE_DIE = 260,
    REPEAT = 261,
    SIDED_DIE_ZERO = 262,
    EXPLOSION = 263,
    IMPLOSION = 264,
    PENETRATE = 265,
    ONCE = 266,
    MACRO_ACCESSOR = 267,
    MACRO_STORAGE = 268,
    SYMBOL_SEPERATOR = 269,
    ASSIGNMENT = 270,
    KEEP_LOWEST = 271,
    KEEP_HIGHEST = 272,
    DROP_LOWEST = 273,
    DROP_HIGHEST = 274,
    FILTER = 275,
    LBRACE = 276,
    RBRACE = 277,
    PLUS = 278,
    MINUS = 279,
    MULT = 280,
    MODULO = 281,
    DIVIDE_ROUND_UP = 282,
    DIVIDE_ROUND_DOWN = 283,
    REROLL = 284,
    SYMBOL_LBRACE = 285,
    SYMBOL_RBRACE = 286,
    STATEMENT_SEPERATOR = 287,
    CAPITAL_STRING = 288,
    DO_COUNT = 289,
    MAKE_UNIQUE = 290,
    NE = 291,
    EQ = 292,
    GT = 293,
    LT = 294,
    LE = 295,
    GE = 296,
    RANGE = 297,
    UMINUS = 298
  };
#endif
/* Tokens.  */
#define NUMBER 258
#define SIDED_DIE 259
#define FATE_DIE 260
#define REPEAT 261
#define SIDED_DIE_ZERO 262
#define EXPLOSION 263
#define IMPLOSION 264
#define PENETRATE 265
#define ONCE 266
#define MACRO_ACCESSOR 267
#define MACRO_STORAGE 268
#define SYMBOL_SEPERATOR 269
#define ASSIGNMENT 270
#define KEEP_LOWEST 271
#define KEEP_HIGHEST 272
#define DROP_LOWEST 273
#define DROP_HIGHEST 274
#define FILTER 275
#define LBRACE 276
#define RBRACE 277
#define PLUS 278
#define MINUS 279
#define MULT 280
#define MODULO 281
#define DIVIDE_ROUND_UP 282
#define DIVIDE_ROUND_DOWN 283
#define REROLL 284
#define SYMBOL_LBRACE 285
#define SYMBOL_RBRACE 286
#define STATEMENT_SEPERATOR 287
#define CAPITAL_STRING 288
#define DO_COUNT 289
#define MAKE_UNIQUE 290
#define NE 291
#define EQ 292
#define GT 293
#define LT 294
#define LE 295
#define GE 296
#define RANGE 297
#define UMINUS 298

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 89 "src/grammar/dice.yacc"

    vec values;

#line 274 "y.tab.c"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */



#ifdef short
# undef short
#endif

/* On compilers that do not define __PTRDIFF_MAX__ etc., make sure
   <limits.h> and (if available) <stdint.h> are included
   so that the code can choose integer types of a good width.  */

#ifndef __PTRDIFF_MAX__
# include <limits.h> /* INFRINGES ON USER NAME SPACE */
# if defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stdint.h> /* INFRINGES ON USER NAME SPACE */
#  define YY_STDINT_H
# endif
#endif

/* Narrow types that promote to a signed type and that can represent a
   signed or unsigned integer of at least N bits.  In tables they can
   save space and decrease cache pressure.  Promoting to a signed type
   helps avoid bugs in integer arithmetic.  */

#ifdef __INT_LEAST8_MAX__
typedef __INT_LEAST8_TYPE__ yytype_int8;
#elif defined YY_STDINT_H
typedef int_least8_t yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef __INT_LEAST16_MAX__
typedef __INT_LEAST16_TYPE__ yytype_int16;
#elif defined YY_STDINT_H
typedef int_least16_t yytype_int16;
#else
typedef short yytype_int16;
#endif

#if defined __UINT_LEAST8_MAX__ && __UINT_LEAST8_MAX__ <= __INT_MAX__
typedef __UINT_LEAST8_TYPE__ yytype_uint8;
#elif (!defined __UINT_LEAST8_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST8_MAX <= INT_MAX)
typedef uint_least8_t yytype_uint8;
#elif !defined __UINT_LEAST8_MAX__ && UCHAR_MAX <= INT_MAX
typedef unsigned char yytype_uint8;
#else
typedef short yytype_uint8;
#endif

#if defined __UINT_LEAST16_MAX__ && __UINT_LEAST16_MAX__ <= __INT_MAX__
typedef __UINT_LEAST16_TYPE__ yytype_uint16;
#elif (!defined __UINT_LEAST16_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST16_MAX <= INT_MAX)
typedef uint_least16_t yytype_uint16;
#elif !defined __UINT_LEAST16_MAX__ && USHRT_MAX <= INT_MAX
typedef unsigned short yytype_uint16;
#else
typedef int yytype_uint16;
#endif

#ifndef YYPTRDIFF_T
# if defined __PTRDIFF_TYPE__ && defined __PTRDIFF_MAX__
#  define YYPTRDIFF_T __PTRDIFF_TYPE__
#  define YYPTRDIFF_MAXIMUM __PTRDIFF_MAX__
# elif defined PTRDIFF_MAX
#  ifndef ptrdiff_t
#   include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  endif
#  define YYPTRDIFF_T ptrdiff_t
#  define YYPTRDIFF_MAXIMUM PTRDIFF_MAX
# else
#  define YYPTRDIFF_T long
#  define YYPTRDIFF_MAXIMUM LONG_MAX
# endif
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned
# endif
#endif

#define YYSIZE_MAXIMUM                                  \
  YY_CAST (YYPTRDIFF_T,                                 \
           (YYPTRDIFF_MAXIMUM < YY_CAST (YYSIZE_T, -1)  \
            ? YYPTRDIFF_MAXIMUM                         \
            : YY_CAST (YYSIZE_T, -1)))

#define YYSIZEOF(X) YY_CAST (YYPTRDIFF_T, sizeof (X))

/* Stored state numbers (used for stacks). */
typedef yytype_int8 yy_state_t;

/* State numbers in computations.  */
typedef int yy_state_fast_t;

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# if defined __GNUC__ && 2 < __GNUC__ + (96 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_PURE __attribute__ ((__pure__))
# else
#  define YY_ATTRIBUTE_PURE
# endif
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# if defined __GNUC__ && 2 < __GNUC__ + (7 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_UNUSED __attribute__ ((__unused__))
# else
#  define YY_ATTRIBUTE_UNUSED
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && ! defined __ICC && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                            \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")              \
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END      \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif

#if defined __cplusplus && defined __GNUC__ && ! defined __ICC && 6 <= __GNUC__
# define YY_IGNORE_USELESS_CAST_BEGIN                          \
    _Pragma ("GCC diagnostic push")                            \
    _Pragma ("GCC diagnostic ignored \"-Wuseless-cast\"")
# define YY_IGNORE_USELESS_CAST_END            \
    _Pragma ("GCC diagnostic pop")
#endif
#ifndef YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_END
#endif


#define YY_ASSERT(E) ((void) (0 && (E)))

#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yy_state_t yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (YYSIZEOF (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (YYSIZEOF (yy_state_t) + YYSIZEOF (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYPTRDIFF_T yynewbytes;                                         \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * YYSIZEOF (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / YYSIZEOF (*yyptr);                        \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, YY_CAST (YYSIZE_T, (Count)) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYPTRDIFF_T yyi;                      \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  25
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   103

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  44
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  13
/* YYNRULES -- Number of rules.  */
#define YYNRULES  61
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  92

#define YYUNDEFTOK  2
#define YYMAXUTOK   298


/* YYTRANSLATE(TOKEN-NUM) -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, with out-of-bounds checking.  */
#define YYTRANSLATE(YYX)                                                \
  (0 <= (YYX) && (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex.  */
static const yytype_int8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_int16 yyrline[] =
{
       0,    99,    99,   101,   104,   106,   111,   119,   164,   168,
     193,   218,   243,   269,   318,   348,   372,   376,   386,   416,
     450,   482,   499,   515,   531,   547,   566,   585,   599,   615,
     630,   646,   652,   674,   698,   721,   744,   767,   791,   813,
     836,   857,   882,   906,   932,   951,   973,   975,   979,  1000,
    1048,  1062,  1080,  1105,  1108,  1108,  1108,  1108,  1108,  1108,
    1111,  1118
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "NUMBER", "SIDED_DIE", "FATE_DIE",
  "REPEAT", "SIDED_DIE_ZERO", "EXPLOSION", "IMPLOSION", "PENETRATE",
  "ONCE", "MACRO_ACCESSOR", "MACRO_STORAGE", "SYMBOL_SEPERATOR",
  "ASSIGNMENT", "KEEP_LOWEST", "KEEP_HIGHEST", "DROP_LOWEST",
  "DROP_HIGHEST", "FILTER", "LBRACE", "RBRACE", "PLUS", "MINUS", "MULT",
  "MODULO", "DIVIDE_ROUND_UP", "DIVIDE_ROUND_DOWN", "REROLL",
  "SYMBOL_LBRACE", "SYMBOL_RBRACE", "STATEMENT_SEPERATOR",
  "CAPITAL_STRING", "DO_COUNT", "MAKE_UNIQUE", "NE", "EQ", "GT", "LT",
  "LE", "GE", "RANGE", "UMINUS", "$accept", "gnoll_statement",
  "sub_statement", "macro_statement", "dice_statement", "math",
  "collapsing_dice_operations", "dice_operations", "die_roll",
  "custom_symbol_dice", "csd", "condition", "die_symbol", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_int16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298
};
# endif

#define YYPACT_NINF (-46)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-1)

#define yytable_value_is_error(Yyn) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int8 yypact[] =
{
      40,    22,   -46,   -46,   -46,   -14,     8,    51,    51,     3,
     -46,   -46,   -46,    62,   -46,    49,    17,   -46,     2,   -46,
       4,   -46,    16,    54,   -46,   -46,    40,    51,    51,    51,
      51,    51,    51,    34,    56,    57,    59,    55,   -46,   -46,
     -23,    63,   -46,     7,   -46,    65,   -46,     7,   -46,    51,
     -46,   -46,    23,    23,   -46,   -46,   -46,   -46,   -46,   -46,
     -46,   -46,   -46,   -46,   -46,   -46,   -46,   -46,    67,    55,
      71,    -2,    15,    83,    68,     1,    69,    62,   -46,    95,
     -46,   -46,   -46,    98,     7,   -46,   -46,   -46,   -46,   -46,
     -46,   -46
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_int8 yydefact[] =
{
       0,    47,    60,    45,    61,     0,     0,     0,     0,     0,
       3,     4,     5,     7,    16,    18,    31,    46,     0,    44,
       0,    50,     0,     0,    15,     1,     0,     0,     0,     0,
       0,     0,     0,    29,    27,    30,    28,     0,    17,    22,
       0,    39,    41,     0,    43,    38,    40,     0,    42,     0,
       8,     2,    13,    14,     9,    12,    10,    11,    25,    23,
      26,    24,    59,    54,    56,    55,    57,    58,     0,     0,
       0,    37,     0,    53,     0,    36,     0,     6,    21,     0,
      20,    35,    33,     0,     0,    49,    34,    32,    48,    19,
      52,    51
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int8 yypgoto[] =
{
     -46,    76,   -46,   -46,   -46,    -7,   -46,   -46,   -46,   -46,
     -45,   -36,   102
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int8 yydefgoto[] =
{
      -1,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      74,    68,    18
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int8 yytable[] =
{
      23,    24,    76,    25,    70,    41,    69,    45,    81,    82,
      72,    86,    87,    62,    63,    64,    65,    66,    67,    21,
      52,    53,    54,    55,    56,    57,     2,    19,    42,     4,
      46,    49,    43,    79,    47,    26,    44,    58,    48,    91,
      73,    22,    77,     1,     2,     3,    40,     4,    29,    30,
      31,    32,     5,     6,     1,     2,     3,    83,     4,    59,
      60,     7,    61,     5,     8,    33,    34,    35,    36,    37,
      78,    71,     7,    75,    80,     8,    50,    27,    28,    29,
      30,    31,    32,    38,    39,    27,    28,    29,    30,    31,
      32,    62,    63,    64,    65,    66,    67,    84,    89,    85,
      88,    90,    51,    20
};

static const yytype_int8 yycheck[] =
{
       7,     8,    47,     0,    40,     3,    29,     3,    10,    11,
       3,    10,    11,    36,    37,    38,    39,    40,    41,    33,
      27,    28,    29,    30,    31,    32,     4,     5,    26,     7,
      26,    15,    30,    69,    30,    32,    34,     3,    34,    84,
      33,    33,    49,     3,     4,     5,    29,     7,    25,    26,
      27,    28,    12,    13,     3,     4,     5,    42,     7,     3,
       3,    21,     3,    12,    24,    16,    17,    18,    19,    20,
       3,     8,    21,     8,     3,    24,    22,    23,    24,    25,
      26,    27,    28,    34,    35,    23,    24,    25,    26,    27,
      28,    36,    37,    38,    39,    40,    41,    14,     3,    31,
      31,     3,    26,     1
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_int8 yystos[] =
{
       0,     3,     4,     5,     7,    12,    13,    21,    24,    45,
      46,    47,    48,    49,    50,    51,    52,    53,    56,     5,
      56,    33,    33,    49,    49,     0,    32,    23,    24,    25,
      26,    27,    28,    16,    17,    18,    19,    20,    34,    35,
      29,     3,    26,    30,    34,     3,    26,    30,    34,    15,
      22,    45,    49,    49,    49,    49,    49,    49,     3,     3,
       3,     3,    36,    37,    38,    39,    40,    41,    55,    29,
      55,     8,     3,    33,    54,     8,    54,    49,     3,    55,
       3,    10,    11,    42,    14,    31,    10,    11,    31,     3,
       3,    54
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_int8 yyr1[] =
{
       0,    44,    45,    45,    46,    46,    47,    48,    49,    49,
      49,    49,    49,    49,    49,    49,    49,    50,    50,    51,
      51,    51,    51,    51,    51,    51,    51,    51,    51,    51,
      51,    51,    52,    52,    52,    52,    52,    52,    52,    52,
      52,    52,    52,    52,    52,    52,    52,    52,    53,    53,
      53,    54,    54,    54,    55,    55,    55,    55,    55,    55,
      56,    56
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     3,     1,     1,     1,     4,     1,     3,     3,
       3,     3,     3,     3,     3,     2,     1,     2,     1,     5,
       4,     4,     2,     3,     3,     3,     3,     2,     2,     2,
       2,     1,     5,     4,     5,     4,     4,     3,     3,     2,
       3,     2,     3,     2,     2,     1,     1,     1,     5,     4,
       2,     3,     3,     1,     1,     1,     1,     1,     1,     1,
       1,     1
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                    \
  do                                                              \
    if (yychar == YYEMPTY)                                        \
      {                                                           \
        yychar = (Token);                                         \
        yylval = (Value);                                         \
        YYPOPSTACK (yylen);                                       \
        yystate = *yyssp;                                         \
        goto yybackup;                                            \
      }                                                           \
    else                                                          \
      {                                                           \
        yyerror (YY_("syntax error: cannot back up")); \
        YYERROR;                                                  \
      }                                                           \
  while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*-----------------------------------.
| Print this symbol's value on YYO.  |
`-----------------------------------*/

static void
yy_symbol_value_print (FILE *yyo, int yytype, YYSTYPE const * const yyvaluep)
{
  FILE *yyoutput = yyo;
  YYUSE (yyoutput);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyo, yytoknum[yytype], *yyvaluep);
# endif
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}


/*---------------------------.
| Print this symbol on YYO.  |
`---------------------------*/

static void
yy_symbol_print (FILE *yyo, int yytype, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyo, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  yy_symbol_value_print (yyo, yytype, yyvaluep);
  YYFPRINTF (yyo, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yy_state_t *yybottom, yy_state_t *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yy_state_t *yyssp, YYSTYPE *yyvsp, int yyrule)
{
  int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %d):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[+yyssp[yyi + 1 - yynrhs]],
                       &yyvsp[(yyi + 1) - (yynrhs)]
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen(S) (YY_CAST (YYPTRDIFF_T, strlen (S)))
#  else
/* Return the length of YYSTR.  */
static YYPTRDIFF_T
yystrlen (const char *yystr)
{
  YYPTRDIFF_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYPTRDIFF_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYPTRDIFF_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            else
              goto append;

          append:
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (yyres)
    return yystpcpy (yyres, yystr) - yyres;
  else
    return yystrlen (yystr);
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYPTRDIFF_T *yymsg_alloc, char **yymsg,
                yy_state_t *yyssp, int yytoken)
{
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat: reported tokens (one for the "unexpected",
     one per "expected"). */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Actual size of YYARG. */
  int yycount = 0;
  /* Cumulated lengths of YYARG.  */
  YYPTRDIFF_T yysize = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[+*yyssp];
      YYPTRDIFF_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
      yysize = yysize0;
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYPTRDIFF_T yysize1
                    = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM)
                    yysize = yysize1;
                  else
                    return 2;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
    default: /* Avoid compiler warnings. */
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    /* Don't count the "%s"s in the final size, but reserve room for
       the terminator.  */
    YYPTRDIFF_T yysize1 = yysize + (yystrlen (yyformat) - 2 * yycount) + 1;
    if (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM)
      yysize = yysize1;
    else
      return 2;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          ++yyp;
          ++yyformat;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
{
  YYUSE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    yy_state_fast_t yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yy_state_t yyssa[YYINITDEPTH];
    yy_state_t *yyss;
    yy_state_t *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYPTRDIFF_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYPTRDIFF_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;


/*------------------------------------------------------------.
| yynewstate -- push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;


/*--------------------------------------------------------------------.
| yysetstate -- set current state (the top of the stack) to yystate.  |
`--------------------------------------------------------------------*/
yysetstate:
  YYDPRINTF ((stderr, "Entering state %d\n", yystate));
  YY_ASSERT (0 <= yystate && yystate < YYNSTATES);
  YY_IGNORE_USELESS_CAST_BEGIN
  *yyssp = YY_CAST (yy_state_t, yystate);
  YY_IGNORE_USELESS_CAST_END

  if (yyss + yystacksize - 1 <= yyssp)
#if !defined yyoverflow && !defined YYSTACK_RELOCATE
    goto yyexhaustedlab;
#else
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYPTRDIFF_T yysize = yyssp - yyss + 1;

# if defined yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        yy_state_t *yyss1 = yyss;
        YYSTYPE *yyvs1 = yyvs;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * YYSIZEOF (*yyssp),
                    &yyvs1, yysize * YYSIZEOF (*yyvsp),
                    &yystacksize);
        yyss = yyss1;
        yyvs = yyvs1;
      }
# else /* defined YYSTACK_RELOCATE */
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yy_state_t *yyss1 = yyss;
        union yyalloc *yyptr =
          YY_CAST (union yyalloc *,
                   YYSTACK_ALLOC (YY_CAST (YYSIZE_T, YYSTACK_BYTES (yystacksize))));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
# undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YY_IGNORE_USELESS_CAST_BEGIN
      YYDPRINTF ((stderr, "Stack size increased to %ld\n",
                  YY_CAST (long, yystacksize)));
      YY_IGNORE_USELESS_CAST_END

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }
#endif /* !defined yyoverflow && !defined YYSTACK_RELOCATE */

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;


/*-----------.
| yybackup.  |
`-----------*/
yybackup:
  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);
  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  /* Discard the shifted token.  */
  yychar = YYEMPTY;
  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
  case 6:
#line 111 "src/grammar/dice.yacc"
                                                {
        // TODO: Is not recalculating if used twice.
        vec key = (yyvsp[-2].values);
        vec value = (yyvsp[0].values);
        register_macro(key.symbols[0], &value);
    }
#line 1526 "y.tab.c"
    break;

  case 7:
#line 119 "src/grammar/dice.yacc"
                    {

    vec vector;
    vec new_vec;
    vector = (yyvsp[0].values);

    new_vec = vector;
    //  Step 1: Collapse pool to a single value if nessicary
    collapse_vector(&vector, &new_vec);

    // Step 2: Output
    FILE *fp;

    if(write_to_file){
        fp = fopen(output_file, "a+");
    }

    for(int i = 0; i!= new_vec.length;i++){
        if (new_vec.dtype == SYMBOLIC){
            // TODO: Strings >1 character
            if (verbose){
                printf("%s;", new_vec.symbols[i]);
            }
            if(write_to_file){
                fprintf(fp, "%s;", new_vec.symbols[i]);
            }
        }else{
            if(verbose){
                printf("%d;", new_vec.content[i]);
            }
            if(write_to_file){
                fprintf(fp, "%d;", new_vec.content[i]);
            }
        }
    }
    if(verbose){
        printf("\n");
    }

    if(write_to_file){
        fclose(fp);
    }
}
#line 1574 "y.tab.c"
    break;

  case 8:
#line 164 "src/grammar/dice.yacc"
                      {
        (yyval.values) =  (yyvsp[-1].values);
    }
#line 1582 "y.tab.c"
    break;

  case 9:
#line 168 "src/grammar/dice.yacc"
                  {
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;
        vector1 = (yyvsp[-2].values);
        vector2 = (yyvsp[0].values);

        if (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC){
            printf("Division unsupported for symbolic dice.");
            YYABORT;
            yyclearin;
        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.content[0] = v1 * v2;
            new_vec.dtype = vector1.dtype;

            (yyval.values) = new_vec;
        }
    }
#line 1611 "y.tab.c"
    break;

  case 10:
#line 193 "src/grammar/dice.yacc"
                             {
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;
        vector1 = (yyvsp[-2].values);
        vector2 = (yyvsp[0].values);

        if (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC){
            printf("Division unsupported for symbolic dice.");
            YYABORT;
            yyclearin;
        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.content[0] = (v1+(v2-1))/ v2;
            new_vec.dtype = vector1.dtype;

            (yyval.values) = new_vec;
        }
    }
#line 1640 "y.tab.c"
    break;

  case 11:
#line 218 "src/grammar/dice.yacc"
                               {
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;
        vector1 = (yyvsp[-2].values);
        vector2 = (yyvsp[0].values);

        if (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC){
            printf("Modulo unsupported for symbolic dice.");
            YYABORT;
            yyclearin;
        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.content[0] = v1 / v2;
            new_vec.dtype = vector1.dtype;

            (yyval.values) = new_vec;
        }
    }
#line 1669 "y.tab.c"
    break;

  case 12:
#line 243 "src/grammar/dice.yacc"
                    {
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;

        vector1 = (yyvsp[-2].values);
        vector2 = (yyvsp[0].values);

        if (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC){
            printf("Modulo unsupported for symbolic dice.");
            YYABORT;
            yyclearin;
        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.content[0] = v1 % v2;
            new_vec.dtype = vector1.dtype;

            (yyval.values) = new_vec;
        }
    }
#line 1699 "y.tab.c"
    break;

  case 13:
#line 269 "src/grammar/dice.yacc"
                  {
        // Collapse both sides and subtract
        vec vector1;
        vec vector2;
        vector1 = (yyvsp[-2].values);
        vector2 = (yyvsp[0].values);

        if (
            (vector1.dtype == SYMBOLIC && vector2.dtype == NUMERIC) ||
            (vector2.dtype == SYMBOLIC && vector1.dtype == NUMERIC)
        ){
            printf("Addition not supported with mixed dice types.");
            YYABORT;
            yyclearin;
        } else if (vector1.dtype == SYMBOLIC){
            vec new_vec;
            unsigned int concat_length = vector1.length + vector2.length;
            new_vec.symbols = calloc(sizeof(char *), concat_length);
            for (int i = 0; i != concat_length; i++){
                new_vec.symbols[i] = calloc(sizeof(char), MAX_SYMBOL_TEXT_LENGTH);
            }
            new_vec.length = concat_length;
            new_vec.dtype = vector1.dtype;

            concat_symbols(
                vector1.symbols, vector1.length,
                vector2.symbols, vector2.length,
                new_vec.symbols
            );
            // free(vector1.symbols);
            // free(vector2.symbols);

            (yyval.values) = new_vec;

        }else{
            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.dtype = vector1.dtype;
            new_vec.content[0] = v1 + v2;

            (yyval.values) = new_vec;
        }

    }
#line 1752 "y.tab.c"
    break;

  case 14:
#line 318 "src/grammar/dice.yacc"
                   {
        vec vector1;
        vec vector2;
        vector1 = (yyvsp[-2].values);
        vector2 = (yyvsp[0].values);
        if (
            (vector1.dtype == SYMBOLIC || vector2.dtype == SYMBOLIC)
        ){
            // It's not clear whether {+,-} - {-, 0} should be {+} or {+, 0}!
            // Therfore, we'll exclude it.
            printf("Subtract not supported with symbolic dice.");
            YYABORT;
            yyclearin;
        }else{
            // Collapse both sides and subtract

            int v1 = collapse(vector1.content, vector1.length);
            int v2 = collapse(vector2.content, vector2.length);

            vec new_vec;
            new_vec.content = calloc(sizeof(int), 1);
            new_vec.length = 1;
            new_vec.content[0] = v1 - v2;
            new_vec.dtype = vector1.dtype;

            (yyval.values) = new_vec;
        }

    }
#line 1786 "y.tab.c"
    break;

  case 15:
#line 348 "src/grammar/dice.yacc"
                           {
        // Eltwise Negation
        vec vector;
        vector = (yyvsp[0].values);

        if (vector.dtype == SYMBOLIC){
            printf("Symbolic Dice, Cannot negate. Consider using Numeric dice or post-processing.");
            YYABORT;
            yyclearin;
        } else {
            vec new_vec;

            new_vec.content = calloc(sizeof(int), vector.length);
            new_vec.length = vector.length;
            new_vec.dtype = vector.dtype;

            for(int i = 0; i != vector.length; i++){
                new_vec.content[i] = - vector.content[i];
            }
            (yyval.values) = new_vec;

        }
    }
#line 1814 "y.tab.c"
    break;

  case 17:
#line 376 "src/grammar/dice.yacc"
                            {

        vec new_vec;
        vec dice = (yyvsp[-1].values);
        initialize_vector(&new_vec, NUMERIC, 1);

        new_vec.content[0] = dice.length;
        (yyval.values) = new_vec;
    }
#line 1828 "y.tab.c"
    break;

  case 18:
#line 386 "src/grammar/dice.yacc"
                   {

        vec vector;
        vector = (yyvsp[0].values);

        if (vector.dtype == SYMBOLIC){
            // Symbolic, Impossible to collapse
            (yyval.values) = vector;
        }
        else{
            // Collapse if Nessicary
            if(vector.length > 1){
                int result = sum(vector.content, vector.length);

                vec new_vector;
                initialize_vector(&new_vector, NUMERIC, 1);
                new_vector.content[0] = sum(vector.content, vector.length);

                (yyval.values) = new_vector;
            }else{
                (yyval.values) = vector;
            }

        }
    }
#line 1858 "y.tab.c"
    break;

  case 19:
#line 416 "src/grammar/dice.yacc"
                                           {

        vec dice = (yyvsp[-4].values);
        int check = (yyvsp[-1].values).content[0];

        if(dice.dtype == NUMERIC){
            int count = 0;
            while (! check_condition(&dice, &(yyvsp[0].values), check)){
                if (count > MAX_ITERATION){
                    printf("MAX ITERATION LIMIT EXCEEDED: REROLL");
                    break;
                }
                vec number_of_dice;
                initialize_vector(&number_of_dice, NUMERIC, 1);
                number_of_dice.content[0] = dice.source.number_of_dice;

                vec die_sides;
                initialize_vector(&die_sides, NUMERIC, 1);
                die_sides.content[0] = dice.source.die_sides;

                roll_plain_sided_dice(
                    &number_of_dice,
                    &die_sides,
                    &dice,
                    dice.source.explode,
                    1
                );
                count ++;
            }
            (yyval.values) = dice;
        }else{
            printf("No support for Symbolic die rerolling yet!");
        }
    }
#line 1897 "y.tab.c"
    break;

  case 20:
#line 450 "src/grammar/dice.yacc"
                                     {

        vec dice = (yyvsp[-3].values);
        int check = (yyvsp[-1].values).content[0];

        if(dice.dtype == NUMERIC){
            if (check_condition(&dice, &(yyvsp[0].values), check)){

                vec number_of_dice;
                initialize_vector(&number_of_dice, NUMERIC, 1);
                number_of_dice.content[0] = dice.source.number_of_dice;

                vec die_sides;
                initialize_vector(&die_sides, NUMERIC, 1);
                die_sides.content[0] = dice.source.die_sides;

                roll_plain_sided_dice(
                    &number_of_dice,
                    &die_sides,
                    &(yyval.values),
                    dice.source.explode,
                    1
                );
            }else{
                // No need to reroll
                (yyval.values) = (yyvsp[-3].values);
            }
        }else{
            printf("No support for Symbolic die rerolling yet!");
        }
    }
#line 1933 "y.tab.c"
    break;

  case 21:
#line 482 "src/grammar/dice.yacc"
                                           {
        vec new_vec;
        vec dice = (yyvsp[-3].values);
        vec condition = (yyvsp[0].values);
        int check = (yyvsp[-1].values).content[0];

        if(dice.dtype == NUMERIC){
            initialize_vector(&new_vec, NUMERIC, dice.length);
            filter(&dice, &condition, check, &new_vec);

            (yyval.values) = new_vec;
        }else{
            printf("No support for Symbolic die rerolling yet!");
        }

    }
#line 1954 "y.tab.c"
    break;

  case 22:
#line 499 "src/grammar/dice.yacc"
                               {
        // TODO
        vec new_vec;
        vec cond_vec;
        vec dice = (yyvsp[-1].values);

        if(dice.dtype == NUMERIC){
            initialize_vector(&new_vec, NUMERIC, dice.length);
            filter_unique(&dice, &new_vec);

            (yyval.values) = new_vec;
        }else{
            printf("No support for Symbolic die rerolling yet!");
        }
    }
#line 1974 "y.tab.c"
    break;

  case 23:
#line 516 "src/grammar/dice.yacc"
    {
        vec keep_vector = (yyvsp[0].values);
        vec new_vec;
        unsigned int num_to_hold = keep_vector.content[0];

        unsigned int err = keep_highest_values(&(yyvsp[-2].values), &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepHighestN.");
            YYABORT;
            yyclearin;
        }
        (yyval.values) = new_vec;
    }
#line 1993 "y.tab.c"
    break;

  case 24:
#line 532 "src/grammar/dice.yacc"
    {
        vec keep_vector = (yyvsp[0].values);
        vec new_vec;
        unsigned int num_to_hold = keep_vector.content[0];

        unsigned int err = drop_highest_values(&(yyvsp[-2].values), &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepHighestN.");
            YYABORT;
            yyclearin;
        }
        (yyval.values) = new_vec;
    }
#line 2012 "y.tab.c"
    break;

  case 25:
#line 548 "src/grammar/dice.yacc"
    {
        vec roll_vector;
        vec keep_vector;
        unsigned int num_to_hold;
        keep_vector = (yyvsp[0].values);
        num_to_hold = keep_vector.content[0];

        vec new_vec;
        unsigned int err = keep_lowest_values(&(yyvsp[-2].values), &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepLowestN.");
            YYABORT;
            yyclearin;
        }
        (yyval.values) = new_vec;
    }
#line 2034 "y.tab.c"
    break;

  case 26:
#line 567 "src/grammar/dice.yacc"
    {
        vec roll_vector;
        vec keep_vector;
        unsigned int num_to_hold;
        keep_vector = (yyvsp[0].values);
        num_to_hold = keep_vector.content[0];

        vec new_vec;
        unsigned int err = drop_lowest_values(&(yyvsp[-2].values), &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepLowestN.");
            YYABORT;
            yyclearin;
        }
        (yyval.values) = new_vec;
    }
#line 2056 "y.tab.c"
    break;

  case 27:
#line 586 "src/grammar/dice.yacc"
    {
        unsigned int num_to_hold = 1;
        vec new_vec;
        unsigned int err = keep_highest_values(&(yyvsp[-1].values), &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepHighest1.");
            YYABORT;
            yyclearin;
        }
        (yyval.values) = new_vec;
    }
#line 2073 "y.tab.c"
    break;

  case 28:
#line 600 "src/grammar/dice.yacc"
    {
        vec roll_vec = (yyvsp[-1].values);
        unsigned int num_to_hold = 1;

        vec new_vec;
        unsigned int err = drop_highest_values(&roll_vec, &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepHighest1.");
            YYABORT;
            yyclearin;
        }
        (yyval.values) = new_vec;
    }
#line 2092 "y.tab.c"
    break;

  case 29:
#line 616 "src/grammar/dice.yacc"
    {
        unsigned int num_to_hold = 1;

        vec new_vec;
        unsigned int err = keep_lowest_values(&(yyvsp[-1].values), &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepHighest1.");
            YYABORT;
            yyclearin;
        }
        (yyval.values) = new_vec;
    }
#line 2110 "y.tab.c"
    break;

  case 30:
#line 631 "src/grammar/dice.yacc"
    {
        vec roll_vec = (yyvsp[-1].values);
        unsigned int num_to_hold = 1;

        vec new_vec;
        unsigned int err = drop_lowest_values(&roll_vec, &new_vec, num_to_hold);

        if(err){
            printf("Error in: KeepHighest1.");
            YYABORT;
            yyclearin;
        }
        (yyval.values) = new_vec;
    }
#line 2129 "y.tab.c"
    break;

  case 31:
#line 647 "src/grammar/dice.yacc"
    {
    }
#line 2136 "y.tab.c"
    break;

  case 32:
#line 653 "src/grammar/dice.yacc"
    {
        int start_from = (yyvsp[-3].values).content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &(yyvsp[-4].values),
            &(yyvsp[-2].values),
            &(yyval.values),
            ONLY_ONCE_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
#line 2161 "y.tab.c"
    break;

  case 33:
#line 675 "src/grammar/dice.yacc"
    {

        int start_from = (yyvsp[-3].values).content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &number_of_dice,
            &(yyvsp[-2].values),
            &(yyval.values),
            ONLY_ONCE_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
#line 2188 "y.tab.c"
    break;

  case 34:
#line 699 "src/grammar/dice.yacc"
    {

        int start_from = (yyvsp[-3].values).content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &(yyvsp[-4].values),
            &(yyvsp[-2].values),
            &(yyval.values),
            PENETRATING_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
#line 2214 "y.tab.c"
    break;

  case 35:
#line 722 "src/grammar/dice.yacc"
    {
        int start_from = (yyvsp[-3].values).content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &number_of_dice,
            &(yyvsp[-2].values),
            &(yyval.values),
            PENETRATING_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
#line 2240 "y.tab.c"
    break;

  case 36:
#line 745 "src/grammar/dice.yacc"
    {

        int start_from = (yyvsp[-2].values).content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &(yyvsp[-3].values),
            &(yyvsp[-1].values),
            &(yyval.values),
            PENETRATING_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
#line 2266 "y.tab.c"
    break;

  case 37:
#line 768 "src/grammar/dice.yacc"
    {

        int start_from = (yyvsp[-2].values).content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &number_of_dice,
            &(yyvsp[-1].values),
            &(yyval.values),
            STANDARD_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
#line 2293 "y.tab.c"
    break;

  case 38:
#line 792 "src/grammar/dice.yacc"
    {
        int start_from = (yyvsp[-1].values).content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &(yyvsp[-2].values),
            &(yyvsp[0].values),
            &(yyval.values),
            NO_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
#line 2318 "y.tab.c"
    break;

  case 39:
#line 814 "src/grammar/dice.yacc"
    {

        int start_from = (yyvsp[-1].values).content[0];

        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_plain_sided_dice(
            &number_of_dice,
            &(yyvsp[0].values),
            &(yyval.values),
            NO_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
#line 2344 "y.tab.c"
    break;

  case 40:
#line 837 "src/grammar/dice.yacc"
    {
        vec dice_sides;
        initialize_vector(&dice_sides, NUMERIC, 1);
        dice_sides.content[0] = 100;

        int err = roll_plain_sided_dice(
            &(yyvsp[-2].values),
            &dice_sides,
            &(yyval.values),
            NO_EXPLOSION,
            1
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
#line 2368 "y.tab.c"
    break;

  case 41:
#line 858 "src/grammar/dice.yacc"
    {

        vec num_dice;
        initialize_vector(&num_dice, NUMERIC, 1);
        num_dice.content[0] = 1;
        vec dice_sides;
        initialize_vector(&dice_sides, NUMERIC, 1);
        dice_sides.content[0] = 100;

        int err = roll_plain_sided_dice(
            &num_dice,
            &dice_sides,
            &(yyval.values),
            NO_EXPLOSION,
            1
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
#line 2396 "y.tab.c"
    break;

  case 42:
#line 883 "src/grammar/dice.yacc"
    {

        int start_from = (yyvsp[-1].values).content[0];

        vec dice_sides;
        initialize_vector(&dice_sides, NUMERIC, 1);
        dice_sides.content[0] = 2;

        int err = roll_plain_sided_dice(
            &(yyvsp[-2].values),
            &dice_sides,
            &(yyval.values),
            NO_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
#line 2423 "y.tab.c"
    break;

  case 43:
#line 907 "src/grammar/dice.yacc"
    {
        int start_from = (yyvsp[-1].values).content[0];

        vec num_dice;
        initialize_vector(&num_dice, NUMERIC, 1);
        num_dice.content[0] = 1;
        vec dice_sides;
        initialize_vector(&dice_sides, NUMERIC, 1);
        dice_sides.content[0] = 2;

        int err = roll_plain_sided_dice(
            &num_dice,
            &dice_sides,
            &(yyval.values),
            NO_EXPLOSION,
            start_from
        );
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
#line 2452 "y.tab.c"
    break;

  case 44:
#line 933 "src/grammar/dice.yacc"
    {
        vec result_vec;
        initialize_vector(&result_vec, SYMBOLIC, (yyvsp[-1].values).content[0]);

        int err = roll_symbolic_dice(
            &(yyvsp[-1].values),
            &(yyvsp[0].values),
            &result_vec
        );
        (yyval.values) = result_vec;
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }

    }
#line 2474 "y.tab.c"
    break;

  case 45:
#line 952 "src/grammar/dice.yacc"
    {
        vec result_vec;
        vec number_of_dice;
        initialize_vector(&result_vec, SYMBOLIC, 1);
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = roll_symbolic_dice(
            &number_of_dice,
            &(yyvsp[0].values),
            &result_vec
        );
        (yyval.values) = result_vec;

        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
#line 2499 "y.tab.c"
    break;

  case 48:
#line 980 "src/grammar/dice.yacc"
    {

        // TODO: Multiple ranges

        vec result_vec;
        initialize_vector(&result_vec, SYMBOLIC, (yyvsp[-4].values).content[0]);

        int err = roll_symbolic_dice(
            &(yyvsp[-4].values),
            &(yyvsp[-1].values),
            &result_vec
        );
        (yyval.values) = result_vec;
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
#line 2523 "y.tab.c"
    break;

  case 49:
#line 1001 "src/grammar/dice.yacc"
    {
        vec csd = (yyvsp[-1].values);
        vec result_vec;
        vec number_of_dice;
        initialize_vector(&number_of_dice, NUMERIC, 1);
        number_of_dice.content[0] = 1;

        int err = 0;

        if (csd.dtype == NUMERIC){
            vec dice_sides;
            vec num_dice;
            initialize_vector(&dice_sides, NUMERIC, 1);
            initialize_vector(&num_dice, NUMERIC, 1);
            initialize_vector(&result_vec, NUMERIC, 1);
            num_dice.content[0] = 1;

            int start_value = csd.content[0];
            int end_value = csd.content[csd.length-1];
            dice_sides.content[0] = end_value - start_value + 1;

            // Range
            err = roll_plain_sided_dice(
                &num_dice,
                &dice_sides,
                &result_vec,
                NO_EXPLOSION,
                start_value
            );

        }else{
            initialize_vector(&result_vec, SYMBOLIC, 1);
            // Custom Symbol
            err = roll_symbolic_dice(
                &number_of_dice,
                &(yyvsp[-1].values),
                &result_vec
            );
        }
        (yyval.values) = result_vec;
        print_err_if_present(err);
        if(err){
            YYABORT;
            yyclearin;
        }
    }
#line 2574 "y.tab.c"
    break;

  case 50:
#line 1048 "src/grammar/dice.yacc"
                                 {
        vec vector;
        vector = (yyvsp[0].values);
        char * name = vector.symbols[0];

        vec new_vector;
        search_macros(name, &new_vector);

        // TODO: Apply rerolls!

        (yyval.values) = new_vector;
    }
#line 2591 "y.tab.c"
    break;

  case 51:
#line 1062 "src/grammar/dice.yacc"
                                       {
        vec l;
        vec r;
        l = (yyvsp[-2].values);
        r = (yyvsp[0].values);

        vec new_vector;
        initialize_vector(&new_vector, SYMBOLIC, l.length + r.length);

        concat_symbols(
            l.symbols, l.length,
            r.symbols, r.length,
            new_vector.symbols
        );
        (yyval.values) = new_vector;

    }
#line 2613 "y.tab.c"
    break;

  case 52:
#line 1080 "src/grammar/dice.yacc"
                       {
        vec start = (yyvsp[-2].values);
        vec end = (yyvsp[0].values);

        int s = start.content[0];
        int e = end.content[0];


        if (s > e){
            printf("Range: %i -> %i\n", s, e);
            printf("Reversed Ranged not supported yet.");
            YYABORT;
            yyclearin;
        }

        int spread = e - s + 1; // 2-2= 1 2-3=2, etc

        vec new_vector;
        initialize_vector(&new_vector, NUMERIC, spread);
        for (int i = 0; i <= (e-s); i++){
            new_vector.content[i] = s+i;
        }
        (yyval.values) = new_vector;
    }
#line 2642 "y.tab.c"
    break;

  case 60:
#line 1111 "src/grammar/dice.yacc"
             {
        vec new_vec;
        initialize_vector(&new_vec, NUMERIC, 1);
        new_vec.content[0] = 1;
        (yyval.values) = new_vec;
    }
#line 2653 "y.tab.c"
    break;

  case 61:
#line 1118 "src/grammar/dice.yacc"
                  {
        vec new_vec;
        initialize_vector(&new_vec, NUMERIC, 1);
        new_vec.content[0] = 0;
        (yyval.values) = new_vec;
    }
#line 2664 "y.tab.c"
    break;


#line 2668 "y.tab.c"

      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */
  {
    const int yylhs = yyr1[yyn] - YYNTOKENS;
    const int yyi = yypgoto[yylhs] + *yyssp;
    yystate = (0 <= yyi && yyi <= YYLAST && yycheck[yyi] == *yyssp
               ? yytable[yyi]
               : yydefgoto[yylhs]);
  }

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = YY_CAST (char *, YYSTACK_ALLOC (YY_CAST (YYSIZE_T, yymsg_alloc)));
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:
  /* Pacify compilers when the user code never invokes YYERROR and the
     label yyerrorlab therefore never appears in user code.  */
  if (0)
    YYERROR;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;


/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;


#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif


/*-----------------------------------------------------.
| yyreturn -- parsing is finished, return the result.  |
`-----------------------------------------------------*/
yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[+*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 1127 "src/grammar/dice.yacc"

/* Subroutines */

typedef struct yy_buffer_state * YY_BUFFER_STATE;
extern int yyparse();
extern YY_BUFFER_STATE yy_scan_string(char * str);
extern void yy_delete_buffer(YY_BUFFER_STATE buffer);

int roll(char * s){
    initialize();
    verbose = 0;
    YY_BUFFER_STATE buffer = yy_scan_string(s);
    yyparse();

    yy_delete_buffer(buffer);
    return 0;
}
int roll_verbose(char * s){
    initialize();
    verbose = 1;
    YY_BUFFER_STATE buffer = yy_scan_string(s);

    yyparse();

    yy_delete_buffer(buffer);
    return 0;
}
int roll_and_write(char * s, char * f){
    /* Write the result to file. */
    write_to_file = 1;
    output_file = f;
    if(verbose) printf("Rolling: %s\n", s);
    return roll(s);
}
int mock_roll(char * s, char * f, int mock_value, int quiet, int mock_const){
    init_mocking(mock_value, mock_const);
    verbose = !quiet;
    return roll_and_write(s, f);
}

char * concat_strings(char ** s, int num_s){
    int size_total = 0;
    int spaces = 0;
    for(int i = 1; i != num_s + 1; i++){
        size_total += strlen(s[i]) + 1;
    }
    if (num_s > 1){
        spaces = 1;
        size_total -= 1;  // no need for trailing space
    }
    char * result;
    result = (char *)calloc(sizeof(char), (size_total+1));

    for(int i = 1; i != num_s + 1; i++){
        strcat(result, s[i]);
        if (spaces && i < num_s){
            strcat(result, " ");    // Add spaces
        }
    }

    return result;

}

int main(int argc, char **str){
    char * s = concat_strings(str, argc - 1);
    return roll_verbose(s);
}

int yyerror(s)
const char *s;
{
    fprintf(stderr, "%s\n", s);

    if(write_to_file){
        FILE *fp;
        fp = fopen(output_file, "a+");
        fprintf(fp, "%s;", s);
        fclose(fp);
    }
    return(1);

}

int yywrap(){
    return (1);
}
void print_err_if_present(int err_code){
    switch(err_code){
        case 1:{
            printf("Negative Dice Sides not Allowed\n");
            break;
        }
    }
}
