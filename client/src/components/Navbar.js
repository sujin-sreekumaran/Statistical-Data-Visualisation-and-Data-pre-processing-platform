import Link from "next/link";

export default function Navbar({ onLogout }) {
  return (
    <nav className="bg-white shadow">
      {/* Add your navbar content here */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            {/* Add logo or site name */}
            <div className="flex-shrink-0 flex items-center">
              <span className="text-xl font-bold">Your Site Name</span>
            </div>
          </div>
          <div className="flex items-center">
            <button
              onClick={onLogout}
              className="ml-4 px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-100"
            >
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
}
