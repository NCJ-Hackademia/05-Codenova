module.exports = {
  content: ["./pages/*.{html,js}", "./index.html", "./js/*.js", "./components/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        // Primary Colors - Deep navy for trust and professional credibility
        primary: {
          DEFAULT: "#1a365d", // navy-800
          50: "#e6f3ff", // navy-50
          100: "#b3d9ff", // navy-100
          200: "#80bfff", // navy-200
          300: "#4da6ff", // navy-300
          400: "#1a8cff", // navy-400
          500: "#1a365d", // navy-500
          600: "#152d4d", // navy-600
          700: "#10243d", // navy-700
          800: "#0b1b2d", // navy-800
          900: "#06121d", // navy-900
        },
        
        // Secondary Colors - Bright teal for innovation and technological confidence
        secondary: {
          DEFAULT: "#38b2ac", // teal-500
          50: "#e6fffa", // teal-50
          100: "#b2f5ea", // teal-100
          200: "#81e6d9", // teal-200
          300: "#4fd1c7", // teal-300
          400: "#38b2ac", // teal-400
          500: "#319795", // teal-500
          600: "#2c7a7b", // teal-600
          700: "#285e61", // teal-700
          800: "#234e52", // teal-800
          900: "#1d4044", // teal-900
        },
        
        // Accent Colors - Warm gold for premium moments and success states
        accent: {
          DEFAULT: "#f6ad55", // orange-300
          50: "#fffbf0", // orange-50
          100: "#fef5e7", // orange-100
          200: "#feebc8", // orange-200
          300: "#fbd38d", // orange-300
          400: "#f6ad55", // orange-400
          500: "#ed8936", // orange-500
          600: "#dd6b20", // orange-600
          700: "#c05621", // orange-700
          800: "#9c4221", // orange-800
          900: "#7b341e", // orange-900
        },
        
        // Background Colors
        background: "#fafafa", // gray-50
        surface: "#ffffff", // white
        
        // Text Colors
        text: {
          primary: "#2d3748", // gray-700
          secondary: "#718096", // gray-500
        },
        
        // Status Colors
        success: "#48bb78", // green-400
        warning: "#ed8936", // orange-500
        error: "#e53e3e", // red-500
        
        // Border Colors
        border: {
          DEFAULT: "#e2e8f0", // gray-200
          light: "#f7fafc", // gray-50
          dark: "#cbd5e0", // gray-300
        },
      },
      
      fontFamily: {
        // Headlines - Inter for modern geometric clarity
        headline: ['Inter', 'sans-serif'],
        sans: ['Inter', 'sans-serif'],
        
        // Body - Source Sans Pro for extended reading
        body: ['Source Sans Pro', 'sans-serif'],
        
        // Accents - Playfair Display for premium moments
        accent: ['Playfair Display', 'serif'],
        
        // CTAs - Inter for brand cohesion
        cta: ['Inter', 'sans-serif'],
      },
      
      fontSize: {
        'hero': ['3.5rem', { lineHeight: '1.1', letterSpacing: '-0.02em' }],
        'display': ['2.5rem', { lineHeight: '1.2', letterSpacing: '-0.01em' }],
        'heading': ['2rem', { lineHeight: '1.3' }],
        'subheading': ['1.5rem', { lineHeight: '1.4' }],
        'body-lg': ['1.125rem', { lineHeight: '1.6' }],
        'body': ['1rem', { lineHeight: '1.6' }],
        'body-sm': ['0.875rem', { lineHeight: '1.5' }],
        'caption': ['0.75rem', { lineHeight: '1.4' }],
      },
      
      boxShadow: {
        'card': '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
        'elevated': '0 10px 25px -3px rgba(0, 0, 0, 0.1)',
        'premium': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
        'viewer': '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
      },
      
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out',
        'slide-up': 'slideUp 0.4s ease-out',
        'scale-in': 'scaleIn 0.3s ease-out',
        'rotate-slow': 'rotate 20s linear infinite',
      },
      
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        scaleIn: {
          '0%': { transform: 'scale(0.95)', opacity: '0' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
      },
      
      transitionDuration: {
        'smooth': '300ms',
        'quick': '200ms',
        'camera': '400ms',
      },
      
      transitionTimingFunction: {
        'smooth': 'ease-out',
      },
      
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '128': '32rem',
      },
      
      borderRadius: {
        'xl': '1rem',
        '2xl': '1.5rem',
        '3xl': '2rem',
      },
      
      backdropBlur: {
        'xs': '2px',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
  ],
}