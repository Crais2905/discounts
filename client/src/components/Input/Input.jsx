export function Input({ placeholder, className, ...props }) {
    return (
      <input
        type="text"
        placeholder={placeholder}
        className={`border p-2 rounded ${className}`}
        {...props}
      />
    );
  }