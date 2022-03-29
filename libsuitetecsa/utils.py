#  Copyright (c) 2022. MarilaSoft.
#  #
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  #
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  #
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


def find_error_shop(type_exception):
    def wrapper(func):
        def deco(*args, **kwargs):
            resp = func(*args, **kwargs)
            if not resp.ok:
                raise type_exception(
                    f"No se pudo llevar a cabo la solicitud -> "
                    f"{resp.status_code}: {resp.reason}"
                )
            return resp.text

        return deco

    return wrapper
